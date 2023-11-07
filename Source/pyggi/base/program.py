"""

This module contains Result, GranularityLevel and Program class.

"""
import os, sys, shutil, json
import time, pathlib, random
import signal, subprocess
import shlex, copy, difflib
from io import StringIO
from abc import ABC, abstractmethod
from distutils.dir_util import copy_tree
from pyggi.utils import read_file, WeightedChoice
from .. import PYGGI_DIR, INF
from ..utils import Logger, convert2str, save_file_st, spaces, read_file, save_file, \
    add_quo, generate_id, txt_xml_filenames, compute_fitness
from xml.etree import ElementTree as et
import matlab.engine

class Result:
    def __init__(self, status, fitness=INF, patch=None, diff=None,
                 text=None, sucss=False, eval=0, invld=0, elapsed=INF):
        """
            Initialize Result Object
          :param self:
          :param status:
          :param fitness:
          :param patch:
          :param diff:
          :param text:
          :param sucss:
          :param eval:
          :param invld:
          :param elapsed:
        """
        self.status = status
        self.fitness = fitness
        self.bst_patch = None
        if patch is not None:
            self.bst_patch = patch.clone()
        self.patches = []
        self.curPatch = ''
        self.diff = diff
        self.sucss = sucss
        self.eval = eval
        self.invld = invld
        self.elapsed = elapsed
        self.text = text
        self.bestprg = ""

    def __repr__(self):
        """
          :param self:  
        """
        res = "fitness: {}; elapsed: {:.2f}; status: {}".format(self.fitness, self.elapsed, self.status)
        # res = "sucss:" + str(self.sucss) + "; fitness:" + str(self.fitness)
        # res += "; elapsed:" + str(self.elapsed)
        # res += "; Patch:" + str(self.patch)  # +";\nDiff:"+ str(self.diff)
        return res


class AbstractEngine(ABC):
    @classmethod
    @abstractmethod
    def get_contents(cls, file_path):
        pass

    @classmethod
    @abstractmethod
    def get_modification_points(cls, contents_of_file):
        pass

    @classmethod
    @abstractmethod
    def get_source(cls, program, file_name, index):
        pass

    @classmethod
    def write_to_tmp_dir(cls, contents_of_file, tmp_path):
        with open(tmp_path, 'w') as tmp_file:
            tmp_file.write(cls.dump(contents_of_file))

    @classmethod
    @abstractmethod
    def dump(cls, contents_of_file):
        pass


class AbstractProgram(ABC):
    """
    Program encapsulates the original source code.
    Currently, PYGGI stores the source code as a list of code lines,
    as lines are the only supported unit of modifications.
    For modifications at other granularity levels,
    this class needs to process and store the source code accordingly
    (for example, by parsing and storing the AST).
    """
    CONFIG_FILE_NAME = '.pyggi.config'
    TMP_DIR = os.path.join(PYGGI_DIR, 'tmp_variants')
    SAVE_DIR = os.path.join(PYGGI_DIR, 'saved_variants')

    def __init__(self, args):
        """
        
        """
        self.args = args
        self.operationTags = args.operationTags.split()
        self.target_files: dict = None
        self.prefix = None
        self.suffix = None
        self.first = 0
        self.operators = []
        self.nr_reactions = 0
        self.initial_fitness = INF
        self.contents = dict()
        self.reaction_mpids = dict()  # Modification point ids of reactions
        self.reactions = dict()  # reactions dictionary from name to reaction id
        self.react_probs = dict()
        self.trg_species = dict()  # target species in the reactions
        self.ing_species = dict()  # pool of species
        self.species = dict()
        self.engines = dict()
        self.specDict = dict()
        self.mp2id = dict()

        self.modification_points = dict()
        self.modification_weights = dict()
        self.new_contents = dict()
        self.init_contents = dict()
        self.BEST = args.target
        self.tags = args.tags.split()

        self.proj_path = os.getcwd()
        if self.args.jobid != "0":
            self.timestamp = self.args.jobid
        else:
            self.timestamp = str(int(time.time()) % 9999000)  # approx. 115 days cycle

        self.path = os.path.abspath(args.project_path.strip())
        self.name = os.path.basename(self.path)

        # Create the temporary directory
        self.create_tmp_variant()

        # Configuration
        self.config = self.load_config()
        self.setup()

        # Associate each file to its engine
        self.eng = None
        self.load_engines()
        # initialize matlab if not using system calls
        if self.args.engine:
            rnd = random.randrange(1, 100)
            res = self.init_matlab(rnd)
            assert rnd * rnd == res, "Matlab.init problem!"

        # Load actual contents using the engines
        self.load_contents()
        # prepare logger in the best folder
        path_name = os.path.join(self.path, "best")
        txt_name = os.path.basename(self.target_files[0])
        txt_name = txt_name.split(".")[0] + "_" + self.timestamp
        self.logger = Logger(txt_name, path_name)
        for t_file in self.target_files:
            self.init_contents[t_file] = copy.deepcopy(self.contents[t_file])
            self.react_probs[t_file] = dict()

        self.err_cnt = 0                # Number of parse errors encountered while evaluations
        # Number of evaluations count
        # this is used to seed Matlab randomization
        self.eval_cnt = int(self.timestamp)
        self.process_tree()
        self.print_tree()
        assert self.modification_points
        assert self.contents
        self.print_reactions()
        self.logger.info("Path to the temporal program variants: {}".format(self.tmp_path))

    def __str__(self):
        """
        
        """
        return "{}({}):{}".format(self.__class__.__name__,
                                  self.path, ",".join(self.target_files))

    def setup(self):
        """
        
        """
        pass

    def print_reactions(self):
        print("List of given reactions in plain text:")
        for target in self.target_files:
            lines = self.get_reactions_text(target, self.contents[target])
            for line in lines:
                print(line, end='')
        print()

    def process_tree(self):
        """
        
        """
        mp = self.modification_points
        for filename in self.target_files:
            length = len(mp[filename])
            contents = self.contents[filename]
            self.reaction_mpids[filename] = dict()  # reactions Modification Point ids
            self.ing_species[filename] = []  # pool species Modification Point ids
            self.trg_species[filename] = []  # target species Modification Point ids
            for k in range(length):
                target = contents.find(mp[filename][k])
                if target.tag == "reaction":
                    rname = target.attrib["name"]
                    self.reaction_mpids[filename][rname] = k
                if target.tag == "species":
                    self.ing_species[filename].append(k)
                if target.tag == "speciesReference":
                    self.trg_species[filename].append(k)

    def reactions2str(self, contents, level=1):
        """
        Given a contents and modification points, prepare its xml
          :param ElementTree[] contents: AST as an array of ElementTree
          :param int level: process until reaction level
          :rtype: string
        """
        res = ""
        for target in contents:
            # print(target.tag, level)
            if target.tag == "reaction":
                res += convert2str(et.tostring(target, method="xml"))
            if level >= 2:
                continue
            for child in target:
                res += self.reactions2str(child, level + 1)

        return res

    def load_config(self):
        """
        
          :param self:
        """
        config_file_name = AbstractProgram.CONFIG_FILE_NAME

        # with open(os.path.join(self.path, config_file_name)) as config_file:
        #     config = json.load(config_file)

        modelName = self.args.subject
        modelID = self.args.model
        # Create configuration dictionary
        config = dict()        
        config['modelName'] = modelName
        config['modelID'] = modelID
        config['modelPath'] = "../Benchmark/" + modelName + "/" + modelName + "-" + modelID
        config['test_command'] = "./run.sh" # HARDCODED #
        # Benchmark/H1/H1-06.sbml
        #t_file = f"Benchmark/{modelName}/{modelName}-{modelID:0>2}.sbml"
        t_file = f"Benchmark/{modelName}/{modelName}-{modelID}.sbml"
        print(os.getcwd())
        self.target_files = [t_file]

        return config

    @classmethod
    @abstractmethod
    def get_engine(cls, file_name):
        pass

    def load_engines(self):
        # Associate each file to its engine
        for file_name in self.target_files:
            self.engines[file_name] = self.__class__.get_engine(file_name)

    def reset_contents(self):
        for t_file in self.target_files:
            self.new_contents[t_file] = copy.deepcopy(self.init_contents[t_file])

    def update_ast(self) -> None:
        for name in self.target_files:
            engine = self.engines[name]
            self.contents[name] = copy.deepcopy(self.new_contents[name])
            self.modification_points[name] = engine.get_modification_points(self.contents[name])
            self.species_lst(name, self.contents[name])
            self.reaction_lst(name, self.contents[name])
            self.process_tree()

    def load_contents(self):
        for name in self.target_files:
            engine = self.engines[name]
            self.contents[name], self.prefix, self.suffix \
                = engine.get_contents(os.path.join(self.path, name), self.tags)
            self.modification_points[name] = engine.get_modification_points(self.contents[name])
            self.species_lst(name, self.contents[name])
            self.reaction_lst(name, self.contents[name])

    def set_weight(self, file_name, index, weight):
        """
        :param file_name: the file containing the modification point
        :param index: the index of the modification point
        :param weight: The modification weight([0,1]) of the modification point
        :type file_name: str
        :type index: int
        :type weight: float
        :return: None
        :rtype: None
        """
        assert 0 <= weight <= 1
        if file_name not in self.modification_weights:
            self.modification_weights[file_name] = [1.0] * len(self.modification_points[file_name])
        self.modification_weights[file_name][index] = weight

    def get_source(self, file_name, index):
        """
        :param file_name: the file containing the modification point
        :param index: the index of the modification point
        :type file_name: str
        :type index: int
        :return: the sources of the modification point
        :rtype: str
        """
        return self.engines[file_name].get_source(self, file_name, index)

    def random_file(self, engine=None):
        files = self.target_files
        if engine:
            files = list(filter(lambda f: self.engines[f] == engine, files))
        return random.choice(files)

    def random_target(self, target_file=None, method="random", prv_tid=-1):
        """
        :param str target_file: The modification point is chosen within target_file
        :param str method: The way how to choose a modification point, *'random'* or *'weighted'*
        :param int prv_tid: previous tag id
        :return: The **index** of modification point
        :rtype: int
        """
        if target_file is None:
            target_file = target_file or random.choice(self.target_files)
        assert target_file in self.target_files
        # assert method in ['random', 'weighted']
        candidates = self.modification_points[target_file]
        if method == 'random':
            return target_file, random.randrange(len(candidates))

        candidates = self.reaction_mpids[target_file]
        if method == 'reaction':
            tid = self.react_probs[target_file].rnd_choice()
            return target_file, tid

        if method == "species":
            candidates = self.ing_species[target_file]
        elif method == "speciesReference":
            candidates = self.trg_species[target_file]

        cnt = 0
        ll = len(candidates)
        while True:
            cnt += 1
            tid = candidates[random.randrange(0, ll)]
            if (self.tag(target_file, tid) == method and tid != prv_tid) or cnt > 50:
                break

        return target_file, tid

    def reaction_lst(self, filename, root):
        """
        Given a root, prepare reaction list
            self.reactions => Dictionary(file_name => Dictionary)
            self.reactions[filename] => Dictionary(name => id)
              e.g. {'reaction1': 'mw6a6837f6_96a0_4e94_8be5_4bded1c7520c', 'reaction2': 'mwce70d8c9_61e3_4f9f_89bb_475933ad4232'}
          :param string filename: target file name
          :param (Element in an ElementTree) root: AST node
          :return type: void
        """
        reactions = root.iter("reaction")
        react_lst = {}
        react_probs = {}
        for react in reactions:
            name = react.attrib["name"]
            react_lst[name] = react.attrib["id"]
            react_probs[name] = 1

        self.nr_reactions = len(react_lst)
        self.reactions[filename] = react_lst
        self.react_probs[filename] = react_probs

    def generate_name(self, f_name, name, ID):
        """
        This function is used generate new names for new reactions,
        Given a file name, identifier name and an ID, generate an unused identifier name
          :param string f_name: target file name
          :param string name: new reaction name string
          :param string ID: new reaction string ID (e.g. mwb5da936c_1228_068e_2dec_053c1eb8dabe)
          :return string: new reaction name (e.g. nreact_1, or nreact_2, etc.)
        """
        num = 1
        while True:
            if name + str(num) in self.reactions[f_name]:
                num += 1
                continue
            name = name + str(num)
            self.reactions[f_name][name] = ID
            break

        return name

    def rename_target(self, f_name, target):
        if target.tag == 'reaction':
            rid = generate_id()  # generate a random reaction id
            target.set('id', rid)
            r_name = self.generate_name(f_name, "reaction_", rid)
            target.set('name', r_name)

    def tag(self, filename, tid):
        """
        AST nodes have tags, like, reaction, species, etc.
        Given a target file and an modification point array index,
            return tag of the target id AST
        :param string filename: file name
        :param int tid: modification point array index
        :rtype: string
        """
        mp = self.modification_points[filename]
        target = self.contents[filename].find(mp[tid])

        return target.tag

    @property
    def tmp_path(self):
        """
        :return: The path of the temporary dirctory
        :rtype: str
        """
        return os.path.join(self.__class__.TMP_DIR, self.name, self.timestamp)

    def create_tmp_variant(self):
        """
        Clean the temporary project directory if it exists.
        :return: None
        """
        pathlib.Path(self.tmp_path).mkdir(parents=True, exist_ok=True)
        copy_tree(self.path, self.tmp_path)

    def remove_tmp_variant(self):
        shutil.rmtree(self.tmp_path)

    def write_to_tmp_dir(self, new_contents):
        """
        Write new contents to the temporary directory of program

        :param new_contents: The new contents of the program.
          Refer to *apply* method of :py:class:`.patch.Patch`
        :type new_contents: dict(str, ?)
        :rtype: None
        """
        for t_file, content in new_contents.items():
            txt_name, xml_name = txt_xml_filenames(t_file, self.tmp_path, self.args.algo)
            # txt_lines = self.get_reactions_text(t_file, self.new_contents[t_file])
            # save_file(txt_name, txt_lines)

            target_str = self.prefix
            for key, value in self.species[t_file].items():
                sid, st = value
                target_str += spaces(6) + st

            target_str += spaces(4) + "</listOfSpecies>\n"
            target_str += spaces(4) + "<listOfReactions>\n"
            target_str += spaces(6) + self.reactions2str(content)
            target_str += self.suffix
            save_file_st(xml_name, target_str)

            # engine = self.engines[t_file]
            # self.write_to_tmp_dir(new_contents[target_file], tmp_path)

    def print_tree(self):
        """
        Some mutation operators use index positions in modification points array, to describe their process
        e.g. 24 in ==> StmtDeletion(('Input/Subtraction/CRN/S3.sbml', 24))

        This function prints modification points array with their tags, so that
        it is possible to follow the numbers used in mutation operators.
        e.g. if a part of the printed tree is:
          24: reaction {'id': 'mwce70d8c9_61e3_4f9f_89bb_475933ad4232', 'name': 'reaction_2', 'reversible': 'false'}
          26: speciesReference {'species': 'mw3fa6661f_7165_46dc_a839_528055767c5f', 'stoichiometry': '1'}
        Now, it can be seen that
            StmtDeletion(('Input/Subtraction/CRN/S3.sbml', 24))
        deletes reaction_2 from the CRN.
        """
        mp = self.modification_points
        for name in self.target_files:
            length = len(mp[name])
            self.mp2id[name] = dict()
            for k in range(length):
                target = self.contents[name].find(mp[name][k])
                self.mp2id[name][mp[name][k]] = k
                text = ''.join(target.itertext()).replace("\n", " ")
                print(str(k) + ": " + target.tag)  # + " " + text.strip())

    def dump(self, contents, file_name):
        """
        Convert contents of file to the source code
        :param contents: The contents of the file which is the parsed form of source code
        :type file_name: ?
        :return: The source code
        :rtype: str
        """
        return self.engines[file_name].dump(contents[file_name])

    def get_modified_contents(self, patch):
        """
        
        
        """
        target_files = self.contents.keys()
        m_points = dict()
        self.new_contents = dict()
        for t_file in target_files:
            m_points[t_file] = copy.deepcopy(self.modification_points[t_file])
            self.new_contents[t_file] = copy.deepcopy(self.contents[t_file])
            edits = list(filter(lambda a: a.target[0] == t_file, patch.edit_list))
            for edit in edits:
                edit.apply(self, self.new_contents, m_points)

        return self.new_contents

    def apply(self, patch):
        """
        This method applies the patch to the target program.
        It does not directly modify the source code of the original program,
        but modifies the copied program within the temporary directory.

        :return: The contents of the patch-applied program, See *Hint*.
        :rtype: dict(str, list(str))

        .. hint::
            - key: The target file name(path) related to the program root path
            - value: The contents of the file
        """
        new_contents = self.get_modified_contents(patch)
        self.write_to_tmp_dir(new_contents)
        return new_contents

    def update_kinetic_law(self, reaction, t_file, old_sid=None):
        '''
        
        '''
        list_of_reactants = reaction.find("listOfReactants")
        # prepare reactants list
        reactants = set()
        if list_of_reactants is not None:
            for ele in list_of_reactants.iter("speciesReference"):
                reactants.add(ele.attrib["species"])

        species = self.species[t_file]
        # remove ci's which are not in reactants
        cis = set()
        for apply in reaction.iter("apply"):
            for ele in apply.iter("ci"):
                txt = ele.text.strip()
                cis.add(txt)
                if txt in reactants:
                    continue
                for spec, sid in species.items():
                    if sid[0] == txt:
                        apply.remove(ele)
                        cis.remove(txt)
                        break

            # add, if any reactant is missing in kinetic law,
            for ele in reactants:
                if not (ele in cis):
                    node = et.Element("speciesReference")
                    node.attrib["species"] = ele
                    node.attrib["stoichiometry"] = "1"
                    apply.insert(0, node)

        return True

    def init_matlab(self, rnd):
        '''
          :param self:
          :param rnd: Random Number
        '''
        cwd = os.getcwd()
        os.chdir(self.proj_path + self.tmp_path[1:]+"/Matlab")
        self.first = 0
        try:
            self.eng = matlab.engine.start_matlab()
            return self.eng.calc_sqr(rnd)
        except Exception as err:
            print("Matlab engine start problem: "+str(err))
            sys.exit(0)
        finally:
            os.chdir(cwd)

    def exec_cmd(self, cmd, timeout=15):
        '''
            Old Method calling via OS calls
        '''
        cwd = os.getcwd()
        os.chdir(self.proj_path + self.tmp_path[1:])
        # myra added an argument to get pid
        process = subprocess.Popen(
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, preexec_fn=os.setsid)
        #            stderr=subprocess.PIPE)
        # myra added next line
        pgrp = os.getpgid(process.pid)
        try:
            start = time.time()
            stdout, stderr = process.communicate(timeout=timeout)
            end = time.time()
            return process.returncode, stdout.decode("ascii"), stderr.decode("ascii"), end - start
        except subprocess.TimeoutExpired:
            # process.terminate()
            os.killpg(pgrp, signal.SIGKILL)
            return None, None, None, time.time() - start
        finally:
            os.chdir(cwd)

    def exec_cmd_engine(self, modelPath, unique_id, timeout=10, partial=1, bug_localization = 0, first=False):
        '''
            Call Matlab engine from python directly
          :param self:
          :param modelPath:
          :param unique_id:
          :param timeout:
          :param partial:
          :param bug_localization:

          :return resultObject:
        '''

        cwd = os.getcwd()
        # modelPath="../Benchmark/H1/H1-104.sbml"
        if self.args.debug:
            print("ModelPath :", modelPath)
            print(self.tmp_path)
        os.chdir(self.tmp_path)
        out = StringIO()
        err = StringIO()
        if partial != 1:
            timeout = 5000
        elif self.first < 1:
            timeout *= 3
        self.eval_cnt += 1
        start = time.time()
        try:
            future = self.eng.main(modelPath, unique_id, timeout, partial, bug_localization,
                                   nargout=1, stderr=err, stdout=out, background=True)
            matlabText = future.result(timeout)
            elapsed = time.time() - start
            if self.args.debug:
                print("Matlab Output:", matlabText) # DEBUG #
            try:
                pos1 = matlabText.find("Fitness:")
                pos1 = pos1 + len("Fitness:")
                pos2 = matlabText.index(";", pos1)
                if self.args.debug:
                    print("Position1:",pos1) # DEBUG #
                    print("Position2:",pos2) # DEBUG #
                val = float(matlabText[pos1:pos2])
                status = "SUCCESS"
                if self.args.debug:
                    print("SUCCESS: Parse from MatlabText")
            except:
                val = INF
                status = 'PARSE_ERROR'
                print("ERROR: Parse Error from MatlabText")
            if self.args.debug:
                print("Value:",val) # DEBUG #
                # Grab just the integer value

            resultObject = Result(status, elapsed=elapsed, fitness=val)
            if self.args.debug:
                print(resultObject)
            self.compute_fitness(resultObject,stdout=matlabText, first=first)
            if 0 <= resultObject.fitness <= self.args.target:
                if self.args.debug:
                    print("Full Evaluation after Zero Fitness")
                # Found target fitness value, re-evaluate with full testSuite
                start = time.time()  
                if self.args.debug:
                    print("ModelPath:", modelPath)
                future = self.eng.main(modelPath, unique_id, timeout, 0, 0,
                                       nargout=1, stderr=err, stdout=out, background=True)
                matlabText = future.result(timeout)
                if self.args.debug:
                    print("Matlab Output:", matlabText)
                elapsed = time.time() - start
                resultObject.elapsed = elapsed
                self.compute_fitness(resultObject, stdout=matlabText)
                if self.args.debug:
                    print("Result Object:", resultObject)
            self.first += 1
        except:  # on any other error
            elapsed = time.time() - start
            if self.args.debug:
                print("ERROR: Unkown Error in exec_cmd_engine")
            resultObject = Result("PARSE_ERROR", fitness=INF, elapsed=elapsed)
            self.err_cnt += 1
            rnd = random.randrange(5, 20)
            self.eng.quit()
            ret = self.init_matlab(rnd)

        finally:
            os.chdir(cwd)
            if self.args.debug:
                print("Result Object:", resultObject) # DEBUG #
            return resultObject

    def copy_err_file(self):
        # o_name, ext = os.path.splitext(os.path.basename(self.target_files[0]))
        # dst = self.path + "/parserr/" + o_name + "_" + self.timestamp + "_" + str(self.err_cnt) + ext
        # src = self.proj_path + self.tmp_path[1:] + "/" + self.target_files[0]
        self.err_cnt += 1
        # cmd = "cp " + src + " " + dst
        # self.exec_cmd(cmd)

    def species_lst(self, f_name, root):
        """
        Given a target file and a root of an AST, prepare the list of species
        Prepares the following information:
             self.species => Dictionary(filename => Dictionary)
             self.species[f_name] => Dictionary(speciesName (string) => tuple(ID, species_xml_text)
             self.specDict => Dictionary(filename => array of strings) , e.g. ['X1', 'Y', 'X2']
          :param string f_name: target file name
          :param 'Element in an ElementTree' root: root for a reaction
          :return type: void
        """
        species = root.iter("species")
        spec_list = dict()
        spec_arr = []
        for spec in species:
            spec.set("name", spec.attrib["name"].upper())
            st = "<species"
            sp_name = ""
            sid = ""
            for key, val in spec.attrib.items():
                st += " " + str(key) + "=" + add_quo(str(val))
                if key == "name":
                    sp_name = val
                    spec_arr.append(sp_name)
                if key == "id": sid = val

            st += "/>\n"
            spec_list[sp_name] = (sid, st)
        self.species[f_name] = spec_list
        self.specDict[f_name] = spec_arr

    def print_info(self):
        for target in self.target_files:
            for key, species in self.species[target].items():
                species, _ = species
                print(key, species, end=' ')
            print()

            for specDict in self.specDict[target]:
                print(specDict, end=' ')
            print()

            for mp in self.modification_points[target]:
                print(mp)
            print()

            for key, react in self.reactions[target].items():
                print(key, react, ";", end=' ')
            print()

    def species_name(self, f_name, sid):
        """
        Given a target file name (f_name) and species id (sid), return the species string name:
          :param string f_name: target sbml file name
          :param string sid: species id (e.g. mw7a5fe946_d001_4fb9_9c3d_fb472fc4e35d)
          :return string: species name (e.g. X1)
        """
        for spec in self.species[f_name]:
            spid, txt = self.species[f_name][spec]
            if spid == sid:
                return spec

        return ""

    def get_species_list(self, f_name, root, before=False):
        """
        Get the species list from a root[] in a reaction
        root[] is a list of species nodes either in a listOfReactants or in a listOfProducts
          :param string f_name: target file name
          :param (ElementTree Node[]) root: reactants node in AST
          :param boolean before: True or false
          :return string: list of species names
        """
        txt = ""
        if root is None:
            return txt
        for item in root:
            sid = item.attrib["species"]
            spec = self.species_name(f_name, sid)
            if before:
                txt += " " + spec
            else:
                txt += spec + " "

        return txt

    def copy_best(self, patch=None, epoch=0, sid=0):
        """
        When a target value is found, during a Local_search,
            best sbml and text files are saved into best folder
            in project folder. If 'S3.sbml' is the target file,
            two files are saved
                 S3_timestamp_epochNumber.sbml ==> sbml file
                 S3_timestamp_epochNumber.txt  ==> clear text format
        """
        for t_file in self.target_files:
            dir_name = os.path.dirname(t_file)
            base_name = os.path.basename(t_file)
            self.save_xml_txt(base_name, dir_name, self.path, patch, epoch)

    def save_xml_txt(self, src_file, src_path, target_path, patch, epoch=0, sid=0):
        """
        When a target value is found, during a Local_search,
            best sbml and text files are saved into best folder
            in project folder. If 'S3.sbml' is the target file,
            two files are saved
                 algorithmName-subjectName-timestamp-epochNumber.sbml
                 algorithmName-subjectName-timestamp-epochNumber.txt
            e.g. GeneticAlgorithm-S1-4-1835960-1.sbml
        """
        temp_file = os.path.join(self.tmp_path, src_path, src_file)
        xml_lines = read_file(temp_file)
        temp_file = os.path.join(src_path, src_file)
        txt_lines = self.get_reactions_text(temp_file, self.new_contents[temp_file])
        txt_lines = "".join(txt_lines) + "\nPatch: \n" + str(patch)
        # prepare file name to save into best folder
        target_path = os.path.join(target_path, "best")
        txt_name, xml_name = txt_xml_filenames(src_file, target_path,
                          self.args.algo, self.timestamp, epoch, sid)
        save_file_st(txt_name, txt_lines)
        save_file(xml_name, xml_lines)

    def get_reactions_text(self, f_name, contents):
        lines = []
        reactions = contents.iter("reaction")
        for root in reactions:
            txt = self.get_reaction_text(f_name, root)
            if txt != "null -> null\n":
                lines.append(txt)

        return lines

    def get_reaction_text(self, f_name, tree):
        """
        given a root for a reaction in AST, prepare clean text for the reaction
          :param string f_name: target file name
          :param (Element in an ElementTree) tree: Node in AST
          :return string: clean text of the reaction (e.g. Y X1 -> null)
        """
        root = tree.find("listOfReactants")
        r_name = tree.attrib["name"] + ": "
        txt = ""
        if not (root is None):
            reactants = root.findall("speciesReference")
            txt = self.get_species_list(f_name, reactants)

        if txt == "":
            txt = "null "
        txt += "->"

        root = tree.find("listOfProducts")
        tmp = ""
        if root is not None:
            products = root.findall("speciesReference")
            tmp = self.get_species_list(f_name, products, True)
        if tmp == "":
            tmp = " null"
        txt += tmp + "\n"

        return r_name + txt

    def evaluate_patch(self, patch, timeout=15, partial=1):
        """
        TODO
          :param self: 
          :param patch: ?
          :param timeout: Double
          :param partial: Logical 
          :return
        """
        # apply + run
        self.apply(patch)
        if self.args.debug:
            print(patch) # DEBUG #
        if self.args.engine:
            modelPath = "../" + self.target_files[0]
            res = self.exec_cmd_engine(modelPath, self.timestamp, timeout=timeout, partial=partial)
            patch.fitness = res.fitness
            patch.elapsed = res.elapsed
            if self.args.debug:
                print("Result in evalPatch:",res)
            return res

        t_cmd = self.config["test_command"]
        modelID = self.config["modelID"]
        uniqueID = self.timestamp
        cmd = "{} {} ".format(t_cmd, self.args.matlab1)
        cmd += "{} {} {} {}".format(modelID, uniqueID, timeout, partial)
        # Function Call into Matlab
        return_code, stdout, stderr, elapsed_time = self.exec_cmd(cmd, timeout)
        # print("Stdout", stdout)
        if return_code is None:  # timeout
            return Result('TIMEOUT', fitness=INF, elapsed=elapsed_time)
        else:
            result = Result('SUCCESS', fitness=INF, elapsed=elapsed_time)
            self.compute_fitness(result, return_code, stdout, stderr, elapsed_time)
            # print("Fitness", result.fitness, end= ' ')
            # Check for invalid fitness
            assert not (result.status == 'SUCCESS' and result.fitness is None)
            
            return result

    def initialize_weights(self, stdout="", first=False):
        pos3 = stdout.find("Probabilities: ")
        if pos3 < 0 and not first:
            return

        if self.args.debug:
            print("Localization Flag:", self.args.probs)
            print("NRReactions:", self.nr_reactions)
        
        # Intialize Weights dictionary
        weights = [0] * self.nr_reactions       
        trg = self.target_files[0]            

        # Assume equal weight and initialize weights array
        for k, key in enumerate(self.reactions[trg]):
            tid = self.reaction_mpids[trg][key]
            weights[k] = 1, tid

        # if not using localization, initialize with equal 
        # weights just for the first time
        if self.args.probs == 0 and first:
            self.react_probs[trg] = WeightedChoice(weights, choice=self.args.probs)
            return
        
        if self.args.debug:
            print("Localization Values:",stdout[pos3:])

        # read probabilities and prepare a dictionary
        probs = stdout[pos3 + 15:].split(";")
        tmp_dic = {}
        for k in range(self.nr_reactions):
            react = probs[k]
            rname, prb = react.split(':')
            tmp_dic[rname.strip()] = float(prb)
        
        if self.args.debug:
            print("TmpDic",tmp_dic)

        # Make sure that they are in the same order as they appear in the sbml file
        for k, key in enumerate(self.reactions[trg]):
            tid = self.reaction_mpids[trg][key]
            weights[k] = tmp_dic[key], tid
            if self.args.debug:
                print("Weights: ",weights[k])
    
        self.react_probs[trg] = WeightedChoice(weights, choice=self.args.probs)

    def get_initial_fitness(self):
        """
        Calculate the initial fitness and localization
            If a localization selected, each reaction is marked as the algorithm calculates 
            If no localization selected, each reaction is equally marked as the fault location [Default]
            If no localization selected, each reaction is randomly marked as the fault location [SoA / Comparision]
          :param self:
          :return double: Fitness Value
        """
        self.first = 0
        extended_timeout = self.args.timeout * 2
        modelPath = "../" + self.target_files[0]
        result = self.exec_cmd_engine(modelPath, self.timestamp, timeout=extended_timeout, partial=0, bug_localization=self.args.probs, first=True)
        if self.args.debug: 
            print("FirstResult",result)
        for trg in self.target_files:
            try:
                print(self.react_probs[trg].arr)
            except:
                print("Missing Dictionary Values")            
        if 0 <= result.fitness < INF:
            return result.fitness
        # Fitness: negative is error
        # Fitness: INF is error
        return INF

    def test_sbml(self, modelPath, timeout=10):
        """
            Run Matlab with full Test Suite and no Localization
          :param self:
          :param subject: string
          :param timeout: double
          :return:        resultObject
        """
        return self.exec_cmd_engine(modelPath, self.timestamp, timeout=timeout, partial=0, bug_localization=0)

    def diff(self, patch) -> str:
        """
        Compare the source codes of original program and the patch-applied program
        using *difflib* module(https://docs.python.org/3.6/library/difflib.html).

        :return: The file comparison result
        :rtype: str
        """
        diffs = ''
        new_contents = self.get_modified_contents(patch)
        for file_name in self.target_files:
            orig = self.dump(self.contents, file_name)
            modi = self.dump(new_contents, file_name)
            orig_list = list(map(lambda s: s + '\n', orig.splitlines()))
            modi_list = list(map(lambda s: s + '\n', modi.splitlines()))
            for diff in difflib.context_diff(orig_list, modi_list,
                                             fromfile="before: " + file_name,
                                             tofile="after: " + file_name):
                diffs += diff
        return diffs
