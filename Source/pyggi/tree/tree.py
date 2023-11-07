import random
from ..base import AbstractEdit
from ..utils import get_parent_id, spaces, generate_id, gen_species_text, add_quo
from copy import deepcopy
from xml.etree import ElementTree as ET

"""
Possible Edit Operators
"""


class StmtReplacement(AbstractEdit):
    def __init__(self, target, ingredient):
        super().__init__()
        self.target = target
        self.ingredient = ingredient

    def apply(self, program, new_contents, m_points):
        # check whether the ingredient exists or not
        i_file, iid = self.ingredient
        ingredient = new_contents[i_file].find(m_points[i_file][iid])
        if ingredient is None:
            return False

        t_file, tid = self.target
        target = new_contents[t_file].find(m_points[t_file][tid])
        if ingredient.tag == "reaction":
            # remove the target and take a copy of the ingredient
            parent = new_contents[t_file].find(m_points[t_file][tid] + '..')
            if not (target is None):
                parent.remove(target)
            target = deepcopy(ingredient)
            # rename the target
            program.rename_target(t_file, target)
            new_contents[t_file][1][2].append(target)
            return True

        old_sid = None
        mp_react_prod, ins_grp = get_parent_id(m_points[t_file][tid], "Reactants")
        mp_reaction, _ = get_parent_id(mp_react_prod, "Reaction")
        if mp_reaction == "." or mp_react_prod == ".":
            return False
        reaction = new_contents[t_file].find(mp_reaction)
        if reaction is None:
            return False
        react_prod = new_contents[t_file].find(mp_react_prod)
        if react_prod is None:
            react_prod = ET.Element(ins_grp)
            reaction.insert(0, react_prod)

        if target is None:
            node = ET.Element("speciesReference")
            node.attrib["species"] = ingredient.attrib["id"]
            node.attrib["stoichiometry"] = "1"
            react_prod.insert(0, node)
        else:
            if not ("species" in target.attrib):
                 return False
            if target.attrib["species"] == ingredient.attrib["id"]:
                return True
            old_sid = target.attrib["species"]
            target.set("species", ingredient.attrib["id"])

        if ins_grp == "listOfProducts":
            return True

        return program.update_kinetic_law(reaction, t_file, old_sid)

    @classmethod
    def create(cls, program, target_file=None, ingr_file=None, method='reaction'):
        if target_file is None:
            target_file = program.random_file()
        if ingr_file is None:
            ingr_file = program.random_file(engine=program.engines[target_file])
        method = "speciesReference"
        ing_method = method
        if method == "speciesReference":
            ing_method = "species"
        assert program.engines[target_file] == program.engines[ingr_file]
        target = program.random_target(target_file, method)
        ingr = program.random_target(ingr_file, ing_method, target[1])
        return cls(target, ingr)


class StmtInsertion(AbstractEdit):
    def __init__(self, target, ingredient):
        super().__init__()
        self.target = target
        self.ingredient = ingredient

    def apply(self, program, new_contents, m_points):
        # check whether the ingredient exists or not
        i_file, iid = self.ingredient
        ingredient = new_contents[i_file].find(m_points[i_file][iid])
        if ingredient is None:
            return False

        t_file, tid = self.target
        if ingredient.tag == "reaction":
            # Take a copy of the ingredient
            target = deepcopy(ingredient)
            # rename the target
            program.rename_target(t_file, target)
            new_contents[t_file][1][2].append(target)
        else:  # if a species is inserted
            reaction = new_contents[t_file].find(m_points[t_file][tid])
            # mp_reaction, _ = get_parent_id(m_points[t_file][tid])
            ins_grp = random.choice(["listOfReactants", "listOfProducts"])
            mp_react_prod = m_points[t_file][tid] + "/" + ins_grp + "[1]"
            # tmp = program.mp2id[self.target[0]][mp_react_prod]
            if mp_react_prod in program.mp2id[self.target[0]]:
                self.target = (self.target[0], program.mp2id[self.target[0]][mp_react_prod])

            if reaction is None or not("id" in ingredient.attrib):
                return False
            react_prod = new_contents[t_file].find(mp_react_prod)
            if react_prod is None:
                react_prod = ET.Element(ins_grp)
                reaction.insert(0, react_prod)
            node = ET.Element("speciesReference")
            node.attrib["species"] = ingredient.attrib["id"]
            node.attrib["stoichiometry"] = "1"
            react_prod.insert(0, node)
            if ins_grp == "listOfProducts":
                return True

            return program.update_kinetic_law(reaction, t_file)

    @classmethod
    def create(cls, program, target_file=None, ingr_file=None, method='reaction'):
        if target_file is None:
            target_file = program.random_file()
        if ingr_file is None:
            ingr_file = program.random_file(engine=program.engines[target_file])
        assert program.engines[target_file] == program.engines[ingr_file]
        ing_method = method
        if method == "speciesReference":
            ing_method = "species"
        target = program.random_target(target_file, "reaction")
        ingr = program.random_target(ingr_file, ing_method, target[1])
        return cls(target, ingr)


class NewReaction(AbstractEdit):
    def __init__(self, target, ingredient=None, direction='after', txt="", xml=""):
        super().__init__()
        self.target = target
        self.ingredient = ingredient
        self.direction = direction
        self.text = txt  # clean text
        self.xml_text = xml  # xml text

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, str(self.target), self.text)

    def apply(self, program, new_contents, modification_points):
        t_file = self.target[0]
        engine = program.engines[t_file]

        ing = engine.clean_tree(self.xml_text)
        new_contents[t_file][1][2].append(ing)

        return

    @classmethod
    def create(cls, program, tfile=None, ifile=None, direction=None, method='reaction'):
        if tfile is None:
            tfile = program.random_file()
        if ifile is None:
            ifile = program.random_file(engine=program.engines[tfile])
        assert program.engines[tfile] == program.engines[ifile]
        method = "reaction"  # force for reaction target
        target = program.random_target(tfile, method)
        r_id = generate_id()
        xml_txt = spaces(6) + "<reaction id=" + add_quo(r_id) + " name="
        r_name = program.generate_name(ifile, "nreact_", r_id)
        xml_txt += add_quo(r_name)
        xml_txt += " reversible='false'>\n        <listOfReactants>\n"

        ids = []
        text = ""
        len_sp = len(program.specDict[tfile])
        num_reactants = num_products = 0
        assert program.args.nspec > 1, "Number of species to use in reactions must be greater than 1."
        # Disallow no operation (null -> null)
        # Allow any other combination
        while num_reactants == 0 and num_products == 0:
            num_reactants = random.randrange(program.args.nspec+1)
            num_products = random.randrange(program.args.nspec+1)
        for k in range(num_reactants):
            r = random.randrange(0, len_sp)
            spec = program.specDict[tfile][r]
            ID, txt = program.species[tfile][spec]
            ids.append(ID)
            text += spec + " "
            xml_txt += gen_species_text(ID)

        if text == "":
            text = "null "
        text += "->"
        xml_txt += spaces(8) + "</listOfReactants>\n"
        xml_txt += spaces(8) + "<listOfProducts>\n"

        num_products = random.randrange(program.args.nspec)
        tmp = ""
        for k in range(num_products):
            r = random.randrange(0, len_sp)
            spec = program.specDict[tfile][r]
            ID, txt = program.species[tfile][spec]
            tmp += " " + spec
            xml_txt += gen_species_text(ID)
        if tmp == "": tmp = " null"
        text += tmp
        xml_txt += spaces(8) + "</listOfProducts>\n"
        xml_txt += spaces(8) + "<kineticLaw>\n" + spaces(10)
        xml_txt += "<math>\n"
        xml_txt += spaces(12) + "<apply>\n" + spaces(14) + "<times/>\n"
        rate_id = generate_id()
        xml_txt += spaces(14) + "<ci> " + rate_id + " </ci>\n"
        for Id in ids:
            xml_txt += spaces(14) + "<ci> " + Id + " </ci>\n"

        xml_txt += spaces(12) + "</apply>\n" + spaces(10) + "</math>\n"
        xml_txt += spaces(10) + "<listOfParameters>\n"
        xml_txt += spaces(12) + "<parameter id='" + rate_id
        xml_txt += "' name='kf' value='1' contant='true'/>\n"
        xml_txt += spaces(10) + "</listOfParameters>\n" + spaces(8)
        xml_txt += "</kineticLaw>\n" + spaces(6) + "</reaction>\n"

        return cls(target, xml=xml_txt, txt=text)


class StmtDeletion(AbstractEdit):
    def __init__(self, target):
        super().__init__()
        self.target = target

    def apply(self, program, new_contents, m_points):
        t_file, tid = self.target
        target = new_contents[t_file].find(m_points[t_file][tid])
        if target is None:
            return True
        if target.tag == "reaction":
            parent = new_contents[t_file].find(m_points[t_file][tid] + '..')
            parent.remove(target)
            # engine.do_delete(program, self, new_contents, m_points)
            return True
        if not ("species" in target.attrib):
            return False
        old_sid = target.attrib["species"]
        mp_react_prod, ins_grp = get_parent_id(m_points[t_file][tid], "Reactants")
        mp_reaction, _ = get_parent_id(mp_react_prod, "Reaction")
        if mp_reaction == "." or mp_react_prod == ".":
            return False
        react_prod = new_contents[t_file].find(mp_react_prod)

        if react_prod is None:
            return True
        react_prod.remove(target)
        reaction = new_contents[t_file].find(mp_reaction)
        if len(new_contents[t_file].find(mp_react_prod)) == 0:
            reaction.remove(react_prod)
        if ins_grp == "listOfProducts":
            return True

        return program.update_kinetic_law(reaction, t_file, old_sid)

    @classmethod
    def create(cls, program, target_file=None, method='reaction'):
        if target_file is None:
            target_file = program.random_file()
        if method == 'reaction' and len(program.reaction_mpids[target_file]) <= 1:
            method = "speciesReference"

        return cls(program.random_target(target_file, method))
