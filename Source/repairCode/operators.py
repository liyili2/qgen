"""
Possible Edit Operators
"""
import random
from abc import ABC
from pyggi.base import BaseOperator
from lxml import etree

## Implement new operators here

class QGateReplacement(StmtReplacement):
    def __init__(self, target, ingredient, target_tag):
        super(QGateReplacement, self).__init__(target, ingredient)
        self.target_tag = target_tag

    def apply(self, program, new_contents, modification_points):
        engine = program.engines[self.target[0]]
        return engine.do_replace(program, self, new_contents, modification_points)

    def do_replace(self, program, new_contents, modification_points):
        target_content = new_contents[self.target[0]]
        ingredient_content = new_contents[self.ingredient[0]]

        # Parse the XML content
        target_tree = etree.fromstring(target_content)

        # Find all elements with the target tag and type='Nor'
        elements = target_tree.xpath(".//{}[@type='Nor']".format(self.target_tag))

        if elements:
            # Choose a random element to replace
            element_to_replace = random.choice(elements)

            # Parse the XML content of the ingredient
            ingredient_tree = etree.fromstring(ingredient_content)

            # Create a new <pexp> element with a different gate but the same type
            new_pexp = etree.Element(self.target_tag)
            new_pexp.set('gate', 'NewGate')  # Replace 'NewGate' with your desired gate
            new_pexp.set('type', 'Nor')

            # Replace the chosen element with the new <pexp> element
            parent = element_to_replace.getparent()
            parent.replace(element_to_replace, new_pexp)

            # Serialize the modified XML back to a string
            new_target_content = etree.tostring(target_tree, pretty_print=True).decode('utf-8')

            return new_target_content

        return target_content


class AddOperator(BaseOperator):
    def __init__(self, name, tags):
        super(AddOperator, self).__init__(name)
        self.tags = tags

    def apply(self, program):
        tree = program.get_tree()
        statement = random.choice(tree.findall(".//statement"))
        tag = random.choice(self.tags)

        # Add a new tag within a random statement
        new_tag = ET.SubElement(statement, tag)
        new_tag.text = f"new_{tag}_{random.randint(1, 100)}"


class RemoveOperator(BaseOperator):
    def __init__(self, name, tags):
        super(RemoveOperator, self).__init__(name)
        self.tags = tags

    def apply(self, program):
        tree = program.get_tree()
        statement = random.choice(tree.findall(".//statement"))
        tag = random.choice(self.tags)

        # Remove a random tag within a random statement
        tags_to_remove = statement.findall(tag)
        if tags_to_remove:
            tag_to_remove = random.choice(tags_to_remove)
            statement.remove(tag_to_remove)
