"""
This module contains Patch class.
"""
# import os
# from copy import deepcopy
from .constants import PRECISION, INF
from jmetal.core.solution import Solution
from pyggi.base import AbstractEdit, Patch

class QPatch(Solution, Patch):
    """

    Patch is a sequence of edit operators: both atomic and custom.
    During search iteration, PYGGI modifies the source code of the target program
    by applying a candidate patch. Subsequently, it runs the test script to collect
    dynamic information, such as the execution time or any other user-provided
    properties, via the predefined format that PYGGI recognises.

    """

    def __init__(self, program, number_of_variables: int = 1, number_of_objectives: int = 1):
        # super(JPPatch, self).__init__(program)
        super(JPPatch, self).__init__(number_of_variables=number_of_variables, number_of_objectives=number_of_objectives)
        self.program = program
        self.edit_list = []
        self.fitness = INF

    # Sort according fitness in decreasing order
    def __lt__(self, other):
        if self.fitness is None: return False
        if other.fitness is None: return True
        if abs(self.fitness - other.fitness) < PRECISION:
            return self.__len__() < other.__len__()

        return self.fitness < other.fitness

    def __repr__(self):
        return '\n'.join(list(map(str, self.edit_list)))

    def __len__(self):
        return len(self.edit_list)

    def add(self, edit, after: bool = False):
        """
        Add an edit to the edit list
        :param edit: The edit to be added
        :param edit: :py:class:`.base.AbstractEdit`
        :param after: bool: insert the operator to the end
        :return: None
        """
        assert isinstance(edit, AbstractEdit)

        if after:
            self.edit_list.append(edit)
            return

        self.edit_list.insert(0, edit)
