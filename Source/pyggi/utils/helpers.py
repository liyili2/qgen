import os, random
from copy import deepcopy
from pyggi import INF


class WeightedChoice:

    def __init__(self, arr: list = [], choice: int = 0):
        self.arr = []
        self.size = len(arr)
        self.choice = choice

        if len(arr) > 0:
            if choice == 0:
                self.prepare_equal_weights(arr)
            else:
                self.prepare_standard(arr)

    def rnd_choice(self):
        return random.choice(sum(([v] * wt for wt, v in self.arr), []))

    def prepare_equal_weights(self, lst: list):
        ll = len(lst)
        for k in range(ll):
            pr, val = lst[k]
            lst[k] = (1, val)

        self.arr = deepcopy(lst)

    def prepare_standard(self, lst: list):
        """
        param lst: is a list of tuples
        Standard weight distribution
        lst is a list of (priority weights and values)
        e.g. assume we have a list of 4 items
            (priority, value)
            (0.0, 'canary')
            (0.0, 'snake')
            (0.5, 'cat')
            (0.7, 'dog')
            (0.8, 'fish')
        total = sum of priorities
        """
        # Round to the nearest 4th digit and calculate
        total = 0
        print("LIST in prepareStandard:", lst)
        self.size = len(lst)  # number of items
        ll = self.size
        for k in range(ll):
            pr = lst[k][0]
            if pr < 0.005:
                pr = 0.005   # assume no item has zero probability
            pr = round(pr*200)
            lst[k] = pr, lst[k][1]
            total += pr

        if total <= self.size:
            self.prepare_equal_weights(lst)
            return

        self.arr = deepcopy(lst)


def MMO_Linear(aux_fitness: float, weight: float = 1):
    return aux_fitness * weight


def three_dint(w, h, d):
    matrix = [[[0 for x in range(d)] for y in range(h)] for z in range(w)]

    return matrix


# Not working for now
# needs to be fixed
def if_exists(patch, prev, limit):
    tmp = []
    ltmp = 0
    for p in patch.edit_list:
        tmp.append(str(p))
        ltmp += 1
    tmp.sort()
    for p in prev:
        lp = len(p)
        if lp != ltmp: continue
        dist = 2 #compare2patches(p, tmp, lp)
        if dist == lp:
            return True

    if len(prev) >= limit: del(prev[0])
    prev.append(tmp)

    return False


def file_extension(file_path):
    """
    param file_path: The path of file
    type file_path: str
    return: file extension
    rtype: str
    """
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def exists(lst, key):
    """
    Check if the key exists in the lst
    :param T[] lst: an array
    :param T key: key to search in the array
    :rtype: boolean
    """
    for item in lst:
        if item == key:
            return True

    return False


def gen_text(lst_len):
    """
    Generate a random hexadecimal text with the given length
    :param int lst_len: length of the text
    :rtype: string
    """
    lst = "abcdef0123456789"
    res = ""
    for k in range(lst_len):
        r = random.randrange(0, 16)
        res += lst[r]

    return res


def gen_species_text(sid):
    """
    Generate species text
    :param string sid: species ID string
    :rtype: string
    """
    txt = spaces(10) + "<speciesReference species=" + add_quo(sid)

    return txt + " stoichiometry='1'/>\n"


def generate_id():
    """
    sbml IDs are in the form of mw6a6837f6_96a0_4e94_8be5_4bded1c7520c
    This function generates a random ID string according to
    the lengths [8, 4, 4, 4, 12]
    rtype: random ID string
    """
    length_lst = [4, 4, 4, 12]
    res = "mw" + gen_text(8)
    for l in length_lst:
        res += "_" + gen_text(l)

    return res


def read_file(file_name):
    """
    Read given file and return string[]
    :param string file_name: file name
    :rtype: string[]
    """
    f = open(file_name, "r")
    lines = [line for line in f if line.strip("\n")]
    f.close()

    return lines


def spaces(n):
    """
    prepare a string containing n spaces
    :param int n: length of the spaces
    :rtype: string
    """
    l = [' '] * n
    return ''.join(l)


def save_file_st(file_name, st):
    """
    Given string st, create a new file and save st in it
    :param string file_name: file name
    :param string st: string to be saved
    :rtype: void
    """
    file = open(file_name, 'w')
    file.write(st)
    file.close()


def add_quo(st):
    """
    Given string st, add quotes to the beginning and end of it
    :param string st: string
    :rtype: string, st with quotes
    """
    return "\"" + st + "\""


def save_file(file_name, lines):
    """
    Save string[] to the file (fname)
    :param string file_name: file name
    :param string[] lines: file in the form of lines
    :rtype: void
    """
    f = open(file_name, "w")
    for line in lines:
        f.write(line)
    f.close()


def parent_id(inp_str):
    """
    Given a modification point string,
    sample string: './model[1]/listOfReactions[1]/reaction[2]/listOfReactants[1]/speciesReference[2]'
    parent string: './model[1]/listOfReactions[1]/reaction[2]/listOfReactants[1]'
    parent tag name: listOfReactants
    return (parent modification point string) and (parent tag name)
    """
    pos1 = inp_str.rfind("]/")
    pos2 = inp_str[:pos1].rfind("[")
    pos3 = inp_str[:pos1 + 1].rfind("]/")

    return inp_str[:pos1 + 1], inp_str[pos3 + 2:pos2]


def get_parent_id(inp_str, target):
    """
    Given a modification point inp_str, and a target,
    find target modification point string for the target parent.
    param string inp_str: input string
            e.g. './model[1]/listOfReactions[1]/reaction[2]/listOfReactants[1]/speciesReference[2]'
    parent string target:  target parent tag
            e.g. target is a Reaction tag
    return tuple (string1, string2)
            string1: parent modification point string
            string2: parent tag name
            e.g. './model[1]/listOfReactions[1]/reaction[2]', reaction
    """
    pos = len(inp_str)
    while pos > 0:
        parent_mp, parent = parent_id(inp_str)

        if target == "Reactants":
            if parent in ["listOfReactants", "listOfProducts"]:
                return parent_mp, parent
        elif target == "Reaction":
            parent_mp2, parent2 = parent_id(parent_mp)
            if parent2 == 'listOfReactions':
                return parent_mp, parent

        inp_str = parent_mp
        pos = len(inp_str)

    return ".", "."


def txt_xml_filenames(t_file, path, algo, timestamp=0, epoch=0, sid=0):
    dir_name = os.path.dirname(t_file)
    base_name = os.path.basename(t_file)
    f_name, ext = os.path.splitext(base_name)
    if epoch > 0:
        f_name = "{}-{}-{}-{}-{}".format(algo, f_name, timestamp, epoch, sid)

    txt_name = os.path.join(path, dir_name, f_name + ".txt")
    xml_name = os.path.join(path, dir_name, f_name + ext)
    return txt_name,  xml_name


def add_quo(st):
    """
    Given string st, add quotes to the beginning and end of it
    :param string st: string
    :rtype: string, st with quotes
    """
    return "\"" + st + "\""


def convert2str(binary_text):
    """
    Convert a binary string to regular string
    """
    res = ""
    for c in binary_text:
        res += chr(c)

    return res


def save_file(fname, lines):
    f = open(fname, "w")
    for line in lines:
        f.write(line)
    f.close()


def random_probabilities(nr: int) -> str:
    """
    Generates random probabilities for the reactions
    Sample output: " Probabilities: 4 0.360;1 0.300;3 0.220;2 0.120;"
    :param nr: int number of reactions
    : return string:
    """
    tp = 1  # total percentage
    res = " Probabilities:"
    total = 0
    for k in range(nr - 1):
        rnd = random.randrange(0, tp * 100)
        res += " {} {:.2f};".format(k, rnd / 100)
        total += rnd / 100
        tp -= (rnd / 100)

    return res + " {} {:.2f};".format(nr - 1, tp)


def compute_fitness(result, sout):
    try:  # "Fitness: 122; Elapsed: 1.8; Probabilities: 4 0.360;1 0.300;3 0.220;2 0.120;"
        pos1 = sout.find("Fitness:")
        pos2 = sout.find(";", pos1)
        result.fitness = float(sout[pos1 + 8: pos2])
        if result.fitness < 0:
            result.fitness = INF
    except ValueError as verr:
        result.fitness = INF
        result.status = 'VALUE_ERROR'
    except Exception as ex:
        result.fitness = INF
        result.status = 'PARSE_ERROR'
