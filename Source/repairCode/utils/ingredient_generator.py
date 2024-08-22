import random
import xml.etree.ElementTree as ET

def random_num():
    return random.randint(-1, 1)


def get_random_op():
    operators = ['+', '-', '*', '/', '%', '^', '$']
    return random.choice(operators)


def nested_vexp():
    pass


def get_identifier():
    pass


class vexp_creation:
    vexp_types = None
    vexp_types_not_nested = None

    def __init__(self):
        self.vexp_types_not_nested = [self.create_vexp_num, self.create_vexp_idexp]
        self.vexp_types = self.vexp_types_not_nested + [self.create_vexp_nested]

    @staticmethod
    def et_vexp_element():
        return ET.Element('vexp')

    def create_vexp_idexp(self):
        idexp = self.et_vexp_element()
        idexp.set('op', 'id')
        idexp.text += get_identifier()
        return idexp

    def create_vexp_num(self):
        vexp = self.et_vexp_element()
        vexp.set('op', 'num')
        vexp.text += random_num()

    def create_vexp_nested(self):
        vexp = self.et_vexp_element()
        vexp.set('op', get_random_op())
        vexp.append(self.create_vexp(self.vexp_types_not_nested))
        vexp.append(self.create_vexp(self.vexp_types_not_nested))
        return vexp

    def create_vexp(self, possible_vexp_types):
        function = random.choice(possible_vexp_types)
        return function()

def create_nextexp():
    pass

def generate_if_block(target_element, ingredient_list):
    if_el = ET.Element("Ifa")
    if_el.append(vexp_creation().create_vexp(vexp_creation.vexp_types))
    if_el.append(create_nextexp)
    if_el.append(create_nextexp)
    return if_el

def generate_ingredients(target_element):
    if target_element.tag == "app":
        return
    elif target_element.tag == "if" or target_element.tag == "pexp":
        return
    pass
