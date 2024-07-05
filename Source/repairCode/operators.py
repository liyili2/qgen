"""
Possible Edit Operators
"""
import random
from abc import ABC
#from pyggi.base import BaseOperator
from lxml import etree
import copy
#from pyggi.tree import AbstractTreeEngine
from pyggi.tree.xml_engine import XmlEngine
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion

## Implement new operators here
class QGateReplacement(StmtReplacement):
    def __init__(self, target, ingredient, target_tag): #input env, set a field about env
        super(QGateReplacement, self).__init__(target, ingredient)
        self.target_tag = target_tag
        # sould input an env for variables, mapping variables to types (Nor,QFT, or nat, or function types,etc)
        #think through the env input, we might not be able to input env
        #since in edit list, each program is replaced by a set of edit list
        #then env in each edit list is different
        #we might need to create field in the parser to make env to be part of the program input
        #setting those fields to be unchangable

    def apply(self, program, new_contents, modification_points):
        print(" Qgate replacement ,apply")
        engine = program.engines[self.target[0]]
        result = engine.do_replace(program, self, new_contents, modification_points)
        # print("Target:", self.target)
        # print("Ingredient:", self.ingredient)
        # print("New Contents:", new_contents[self.target[0]])
        #Debugging: Output the modified XML content
        # modified_content = etree.tostring(new_contents[self.target[0]], pretty_print=True).decode('utf-8')
        # print(f'Modified Content:\n{modified_content}')
        return result

    def do_replace(program, self,new_contents, modification_points):
        print("enter into qgate replacement,replace")
        target_content = new_contents[self.target[0]]
        ingredient_content = new_contents[self.ingredient[0]]

        # Parse the XML content
        target_tree = etree.fromstring(target_content)

        #For the first try, replacement should first look at tag having name pair
        #we only allow to modify things inside pairs
        #elements = target_tree.xpath(".//{}[@name='pair']".format(self.target_tag))
        #second, we can locate two groups of gates
        #we should locate pexp tag name, with its id
        #this is to do replacement on pexp. e.g.
        #elements = target_tree.xpath(".//{}[@name = 'pexp']".format(self.target_tag))
        #getids = elements.xpath(... [@id]...)
        #for each id, we check its type in env
        #if env is of type Nor(m), then we can replace the gate to
        #X, CU, SKIP, QFT, Lshift, Rshift, and Rev (the last three are not necessary at this point)
        #QFT is a more costly gate than the other (setting fitness to make it more costly)
        #when apply QFT, the variable id's type env is switch from Nor to Phi(m)
        # when replacing the gate, we need to say make sure that the vexp inside is less than m

        #if env is of type Phi(m), we can replace it with SR or RQFT, or SKIP
        # when replacing the gate with SR, or RQFT, we need to say make sure that the vexp inside is less than m
        #when replacing the gate with RQFT, the type is transferred from phi(m) to Nor

        elements = target_tree.xpath(".//{}[@gate='X' or @gate='CU' or @gate='RZ' or @gate='SKIP']".format(self.target_tag))

        if elements:
            print("enter into qgate replacement,elements")
            # Choose a random element to replace
            element_to_replace = random.choice(elements)

            # Determine the current gate
            current_gate = element_to_replace.get('gate')

            # Define a list of alternative gates
            alternative_gates = ['X', 'CU', 'RZ', 'SKIP']
            alternative_gates.remove(current_gate)

            # Choose a random alternative gate
            new_gate = random.choice(alternative_gates)
            
            # Create a new <pexp> element with the chosen alternative gate but the same 
            new_pexp = etree.Element(self.target_tag)
            new_pexp.set('gate', new_gate)
            
            # Replace the chosen element with the new <pexp> element
            parent = element_to_replace.getparent()
            parent.replace(element_to_replace, new_pexp)
            
            # Serialize the modified XML back to a string
            new_target_content = etree.tostring(target_tree, pretty_print=True).decode('utf-8')
            return new_target_content

        return target_content

    @classmethod
    def create(cls, program, target_file=None, ingr_file=None, method='random'):
        # If no target file is specified, select a random file from the program using the XmlEngine.
        if target_file is None:
            target_file = program.random_file(XmlEngine)
         # If no ingredient file is specified, select a random file from the program using the engine.
       
        if ingr_file is None:
            ingr_file = program.random_file(engine=program.engines[target_file])

        # Ensure that the engines of the target file and the ingredient file are the same.
        assert program.engines[target_file] == program.engines[ingr_file]
        return cls(program.random_target(target_file, method),
                   program.random_target(ingr_file, 'random'),
                   'quantumtag')



class QGateInsertion(StmtInsertion):
    def __init__(self, target, ingredient, direction='before'):
        super(QGateInsertion, self).__init__(target, ingredient, direction)

    def apply(self, program, new_contents, modification_points):
        print("Qgate insertion apply")
        engine = program.engines[self.target[0]]
        result = self.do_insert(program, new_contents, modification_points)
        return result

    # def do_insert(self, program, new_contents, modification_points):
    #     target_content = new_contents[self.target[0]]
    #     ingredient_content = new_contents[self.ingredient[0]]

    #     # Parse the XML content
    #     target_tree = etree.fromstring(target_content)
    #     ingredient_tree = etree.fromstring(ingredient_content)

    #     target_element = target_tree.xpath(modification_points[self.target[0]][self.target[1]])[0]
    #     ingredient_element = ingredient_tree.xpath(modification_points[self.ingredient[0]][self.ingredient[1]])[0]
        
    #     # Get the parent of the target element and the index of the target element within the parent
    #     parent = target_element.getparent()
    #     index = parent.index(target_element)

    #     # Insert the ingredient element into the target's parent
    #     if self.direction == 'before':
    #         parent.insert(index, copy.deepcopy(ingredient_element))
    #     else:
    #         parent.insert(index + 1, copy.deepcopy(ingredient_element))
        
    #     # Serialize the modified XML back to a string
    #     new_target_content = etree.tostring(target_tree, pretty_print=True).decode('utf-8')
    #     return new_target_content
    
    def do_insert(self, program, new_contents, modification_points):
        target_content = new_contents[self.target[0]]
        
        # Parse the XML content
        target_tree = etree.fromstring(target_content)
        
        # Find the target element based on the modification point
        target_element = target_tree.xpath(modification_points[self.target[0]][self.target[1]])[0]
        
        # Get the parent of the target element and the index of the target element within the parent
        parent = target_element.getparent()
        index = parent.index(target_element)

        # Create new <app> element
        app_element = etree.Element('app', id='new_f')
        etree.SubElement(app_element, 'vexp', op='id').text = 'x'
        etree.SubElement(app_element, 'vexp', op='id').text = 'm'
        etree.SubElement(app_element, 'vexp', op='id').text = 'size'
        etree.SubElement(app_element, 'vexp', op='id').text = 'M'

        # Insert the <app> element into the target's parent
        if self.direction == 'before':
            parent.insert(index, copy.deepcopy(app_element))
        else:
            parent.insert(index + 1, copy.deepcopy(app_element))
        
        # Serialize the modified XML back to a string
        new_target_content = etree.tostring(target_tree, pretty_print=True).decode('utf-8')
        new_contents[self.target[0]] = new_target_content  # Update the new contents with modified XML
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
        return cls(program.random_target(target_file, method),
                   program.random_target(ingr_file, 'random'),
                   direction)


class QGateDeletion(StmtDeletion):
    def __init__(self, target):
       super(QGateDeletion, self).__init__(target)

    def apply(self, program, new_contents, modification_points):
        print("Qgate deletion apply")
        engine = program.engines[self.target[0]]
        result = engine.do_delete(program, self, new_contents, modification_points)
        # print("Target:", self.target)
        # print("New Contents:", new_contents[self.target[0]])
        # Debugging: Output the modified XML content
        # modified_content = etree.tostring(new_contents[self.target[0]], pretty_print=True).decode('utf-8')
        # print(f'Modified Content:\n{modified_content}')
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
    

