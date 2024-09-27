"""
Possible Edit Operators
"""
import copy
import random
import xml.etree.ElementTree as ET

from lxml import etree

from Source.quantumCode.AST_Scripts.TypeDetector import TypeDetector
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
from pyggi.tree.xml_engine import XmlEngine
from quantumCode.AST_Scripts.TypeChecker import TypeChecker
from quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from repairCode.configs.type_env import type_envs
from repairCode.utils.ingredient_generator import IngredientGenerator
from repairCode.utils.operator_utils import convert_xml_element_to_ast, convert_xml_element_to_string, pretty_print_element, delete_block


# class QGateReplacement(StmtReplacement):
#     def __init__(self, target, ingredient, target_tag):
#         super(QGateReplacement, self).__init__(target, ingredient)
#         self.target_tag = target_tag
#
#     def apply(self, program, new_contents, modification_points):
#         print(" Qgate replacement, apply")
#         engine = program.engines[self.target[0]]
#         result = self.__class__.do_replace(self, program, new_contents, modification_points)
#         return result
#
#     def do_replace(self, program, new_contents, modification_points):
#         print("enter into qgate replacement, replace")
#         target_content = new_contents[self.target[0]]
#         ingredient_content = new_contents[self.ingredient[0]]
#
#         # Parse the XML content
#         target_tree = etree.fromstring(target_content)
#         elements = target_tree.xpath(
#             ".//{}[@gate='X' or @gate='CU' or @gate='RZ' or @gate='SKIP']".format(self.target_tag))
#
#         if elements:
#             print("enter into qgate replacement, elements")
#             # Choose the specific element to replace based on modification points
#             target_element = target_tree.xpath(modification_points[self.target[0]][self.target[1]])[0]
#             print("target_element before replace:", etree.tostring(target_element))
#
#             current_gate = target_element.get('gate')
#
#             alternative_gates = ['X', 'CU', 'RZ', 'SKIP']
#             alternative_gates.remove(current_gate)
#
#             new_gate = random.choice(alternative_gates)
#             new_pexp = etree.Element(self.target_tag)
#             new_pexp.set('gate', new_gate)
#             new_pexp.set('id', target_element.get('id'))  # Ensure ID is preserved if needed
#
#             # Copy the children (vexp elements) from the original target element
#             for child in target_element:
#                 new_pexp.append(copy.deepcopy(child))
#
#             parent = target_element.getparent()
#             print("parent before replace:", etree.tostring(parent))
#             parent.replace(target_element, new_pexp)
#             print("parent after replace:", etree.tostring(parent))
#
#             new_target_content = etree.tostring(target_tree, pretty_print=True).decode('utf-8')
#             new_contents[self.target[0]] = new_target_content  # Update the new contents with modified XML
#             print("new_target_content:", new_target_content)
#             return True
#
#         return False
#
#     @classmethod
#     def create(cls, program, target_file=None, ingr_file=None, method='random'):
#         if target_file is None:
#             target_file = program.random_file(XmlEngine)
#         if ingr_file is None:
#             ingr_file = program.random_file(engine=program.engines[target_file])
#         assert program.engines[target_file] == program.engines[ingr_file]
#
#         # modify here
#         # 1. program.app_target(target_file, method)
#         # 2. program.app_target(ingr_file, 'random')
#         # 3. you will be able to see candidates here.
#         # 4. based on the candidates, you will do selection and perform different actions.
#         # 5. figure out what is the pexp type -- what the gate is
#         # 5.5, need to look at type env. variables map to types
#         # 6. if gate is SKIP, SKIP can be replaced to the right types,
#         # for example, if you look at the id, id = 'x' , then find x, then find x in the env ---> Nor/Phi
#         # for Nor, SKIP can be replaced by X, CU, QFT, for Phi, SKIP can be replaced by SR, RQFT
#         # 7. if gate is SR, it means that the id has Phi type, SR can be replaced by SR or SKIP
#         # 8. if gate is X, it means that the id of the gate is Nor type,
#         # X can be replaced by SKIP, or CU, but when replaced it with CU, need more work, CU has next level.
#         # 9. if gate is CU, it means that the id is Nor type, and it can be replaced by X, SKIP, with spectial treament
#
#         return cls(program.random_target(target_file, method),
#                    program.random_target(ingr_file, 'random'),
#                    'pexp')


class QGateReplacement(StmtReplacement):

    def __init__(self, target, ingredient):
        super(QGateReplacement, self).__init__(target, ingredient)

    def apply(self, program, contents, modification_points):
        engine = program.engines[self.target[0]]
        # Currently only works for vexp replacements
        result = self._apply_to_vexp(program, contents, modification_points, engine)
        return result

    def _get_xml_for_root_element(self, contents):
        return contents[self.target[0]].find('.')

    def _get_ast_for_root_element(self, contents):
        root = contents[self.target[0]].find('.')
        return convert_xml_element_to_ast(root)

    def get_type_environment(self, contents, initial_type_environment):
        root = self._get_ast_for_root_element(contents)
        type_checker = TypeChecker(initial_type_environment)
        type_checker.visit(root)
        return type_checker.type_environment

    @staticmethod
    def _generate_vexp_replacement_ingredient(checked_type_environment):
        ingr_gen = IngredientGenerator(checked_type_environment)
        ingr_vexp = ingr_gen.generate_vexp()

        return ingr_vexp

    def _apply_to_vexp(self, program, contents, modification_points, engine):
        target_file, target_idx = self.target

        root_contents = self._get_xml_for_root_element(contents)
        ingr_vexp = self._generate_vexp_replacement_ingredient(type_envs[target_file])

        # Replace using "insertion"-like approach
        target = contents[target_file].find(modification_points[target_file][target_idx])
        parent = contents[target_file].find(modification_points[target_file][target_idx] + '..')

        if target is None or ingr_vexp is None:
            return False

        print("Before:\n")
        print(pretty_print_element(root_contents))

        for i, child in enumerate(parent):
            if child == target:
                tmp = copy.deepcopy(ingr_vexp)
                tmp.tail = child.tail
                child.tail = None

                parent.insert(i, tmp)
                parent.remove(child)
                break

        print("After:\n")
        print(pretty_print_element(root_contents))

        return True

    @classmethod
    def create(cls, program, target_file=None, ingr_file=None, direction=None, method='random'):
        if target_file is None:
            target_file = program.random_file(XmlEngine)
        if ingr_file is None:
            ingr_file = program.random_file(engine=program.engines[target_file])
        assert program.engines[target_file] == program.engines[ingr_file]
        if direction is None:
            direction = random.choice(['before', 'after'])
        return cls(program.replace_target(target_file, method), program.replace_target(ingr_file, 'random'))


class QGateInsertion(StmtInsertion):
    def __init__(self, target, ingredient, direction='before'):
        super(QGateInsertion, self).__init__(target, ingredient, direction)

    def apply(self, program, new_contents, modification_points):
        engine = program.engines[self.target[0]]
        result = self.do_insert(self, program, self, new_contents, modification_points, engine)
        return result

    def insert_adjacent_to_target(self, parent, target, ingredient):
        for i, child in enumerate(parent):
            if child == target:
                tmp = copy.deepcopy(ingredient)
                if self.direction == 'after':
                    tmp.tail = child.tail
                    child.tail = None
                    i += 1
                else:
                    tmp.tail = None
                parent.insert(i, tmp)
                break

    def do_insert(self, cls, program, op, new_contents, modification_points, engine):
        def choose_ingredient():
            return IngredientGenerator(checked_type_env).generate_ingredients()
        def check_type(init_type_env):
            root = new_contents[op.target[0]].find('.')
            converted_root = convert_xml_element_to_ast(root)
            type_checker = TypeChecker(init_type_env)
            type_checker.visit(converted_root)
            return type_checker.type_environment

        # get elements
        target = new_contents[op.target[0]].find(modification_points[op.target[0]][op.target[1]])
        parent = new_contents[op.target[0]].find(modification_points[op.target[0]][op.target[1]] + '..')
        ingredient = program.contents[op.ingredient[0]].find(
            program.modification_points[op.ingredient[0]][op.ingredient[1]])

        if target is None or ingredient is None:
            return False

        initial_type_env = type_envs[op.target[0]]
        checked_type_env = check_type(initial_type_env)
        block_el = ET.Element("block")
        self.insert_adjacent_to_target(parent, target, block_el)
        root_element: ET.Element = new_contents[op.target[0]].find('.')
        root_ast_element: XMLExpParser.RootContext = convert_xml_element_to_ast(root_element)
        print("env before", checked_type_env)
        cop = checked_type_env.copy()
        type_detector = TypeDetector(checked_type_env)
        type_detector.visit(root_ast_element)
        print("env after", type_detector.type_environment)
        delete_block(parent)
        self.insert_adjacent_to_target(parent, target, ingredient)

        def update_modification_points():
            head, tag, pos, _ = engine.split_xpath(modification_points[op.target[0]][op.target[1]])
            for i, xpath in enumerate(modification_points[op.target[0]]):
                if i < op.target[1]:
                    continue
                h, t, p, s = engine.split_xpath(xpath, head)
                if h != head and xpath != 'deleted':
                    break
                if t == tag and p == pos and op.direction == 'after':
                    continue
                if t in [ingredient.tag, tag]:
                    if s:
                        new_pos = '{}/{}[{}]/{}'.format(h, t, p + 1, s)
                    else:
                        new_pos = '{}/{}[{}]'.format(h, t, p + 1)
                    modification_points[op.target[0]][i] = new_pos
        update_modification_points()
        return True

    @classmethod
    def create(cls, program, target_file=None, ingr_file=None, direction=None, method='random'):
        if target_file is None:
            target_file = program.random_file(XmlEngine)
        if ingr_file is None:
            ingr_file = program.random_file(engine=program.engines[target_file])
        assert program.engines[target_file] == program.engines[ingr_file]
        if direction is None:
            direction = random.choice(['before', 'after'])
        return cls(program.app_target(target_file, method), program.app_target(ingr_file, 'random'), direction)
    #modify here
    #1. program.app_target(target_file, method)
    #2. program.app_target(ingr_file, 'random')
    #3. you will be able to see candidates here.
    # app/if/pexp
    # if see app, then only allowed if, and pexp
    #if see if/pexp.
    # choose a variable, will have the env to tell you what variables are aviable
    # perform if/pexp on the variable
    #look at the type of the variable in env, if it is Phi, then use SR/RQFT gate only
    #if it is Nor, then use X, CU,
    #if it is nat, can only use if with two branching


class QGateDeletion(StmtDeletion):
    def __init__(self, target):
        super(QGateDeletion, self).__init__(target)



    def apply(self, program, new_contents, modification_points):
        print("Qgate deletion apply")
        engine = program.engines[self.target[0]]
        result = engine.do_delete(program, self, new_contents, modification_points)
        return result

    def do_delete(self, program, new_contents, modification_points):
        target_content = new_contents[self.target[0]]

        target_tree = etree.fromstring(target_content)
        target_element = target_tree.xpath(modification_points[self.target[0]][self.target[1]])[0]
        parent = target_element.getparent()
        parent.remove(target_element)

        new_target_content = etree.tostring(target_tree, pretty_print=True).decode('utf-8')
        return new_target_content

    @classmethod
    def create(cls, program, target_file=None, method='random'):
        if target_file is None:
            target_file = program.random_file(XmlEngine)
        return cls(program.random_target(target_file, method))
