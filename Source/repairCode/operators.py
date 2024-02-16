"""
Possible Edit Operators
"""
import random
from abc import ABC
from pyggi.base import BaseOperator

## Implement new operators here

class ReplaceOperator(BaseOperator):
    def __init__(self, name, tag, quantum_gates):
        super(ReplaceOperator, self).__init__(name)
        self.tag = tag
        self.quantum_gates = quantum_gates

    def apply(self, program):
        tree = program.get_tree()
        statement = tree.findall(tag)

        # Replace the current quantum gate with a random selection
        statement.text = random.choice(self.quantum_gates)


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
