"""
This module contains Patch class.
"""
from __future__ import annotations
from copy import deepcopy
from . import AbstractEdit
from .. import INF
from .program import AbstractProgram
from ..jmetal.core.solution import Solution


class Patch(Solution):
    """

    Patch is a sequence of edit operators: both atomic and custom.
    During search iteration, PyGGI modifies the source code of the target program
    by applying a candidate patch. Subsequently, it runs the test script to collect
    dynamic information, such as the execution time or any other user-provided
    properties, via the predefined format that PyGGI recognises.
    """
    def __init__(self, program: AbstractProgram, number_of_variables: int = 1, number_of_objectives: int = 1):
        # super(JPPatch, self).__init__(program)
        super(Patch, self).__init__(number_of_variables=number_of_variables, number_of_objectives=number_of_objectives)
        self.program: AbstractProgram = program
        self.edit_list: list = []
        self.fitness: float = INF
        self.modified: bool = True
        self.elapsed = 0

    # Sort according fitness in decreasing order
    def __repr__(self) -> str:
        return '\n'.join(list(map(str, self.edit_list))) + " {:.0f}".format(self.fitness)

    def __len__(self) -> int:
        return len(self.edit_list)

    def __lt__(self, other: Patch) -> bool:
        if self.fitness == INF:
            return False
        if abs(self.fitness - other.fitness) < 0.0001:
            return self.__len__() < other.__len__()

        return self.fitness < other.fitness

    def __eq__(self, other: Patch) -> bool:
        if len(self.edit_list) != len(other.edit_list):
            return False
        for k, el in enumerate(self.edit_list):
            if el != other.edit_list[k]:
                return False
        return True
        # return self.edit_list == other.edit_list

    def __le__(self, other: Patch) -> bool:
        return self < other or self == other

    def clone(self) -> Patch:
        """
        Create a new patch which has the same sequence of edits with the current one.

        :return: The created Patch
        :rtype: :py:class:`.Patch`
        """
        clone_patch = Patch(self.program, number_of_variables=self.number_of_variables, \
                            number_of_objectives=self.number_of_objectives)
        clone_patch.edit_list = deepcopy(self.edit_list)
        clone_patch.fitness = self.fitness
        clone_patch.modified = self.modified
        clone_patch.elapsed = self.elapsed
        clone_patch.program = self.program
        return clone_patch

    @property
    def diff(self):
        return self.program.diff(self)

    def edit(self, edit: AbstractEdit, index: int = 0):
        """
        Add an edit to the edit list
        :param edit: The edit to be added
        :param index: index of edit_list
        :type edit: :py:class:`.base.AbstractEdit`
        :return: None
        """
        assert isinstance(edit, AbstractEdit)
        if index < 0 or index >= len(self.edit_list):
            return

        self.edit_list[index] = deepcopy(edit)

    def add(self, edit: AbstractEdit):
        """
        Add an edit to the edit list
        :param after: if true, the patch is added to the end
        :param edit: The edit to be added
        :type edit: :py:class:`.base.AbstractEdit`
        :return: None
        """
        assert isinstance(edit, AbstractEdit)

        if type(edit) == 'NewReaction':
            self.edit_list.append(edit)
            return

        self.edit_list.insert(0, edit)

    def remove(self, index: int):
        """
        Remove an edit from the edit list

        :param int index: The index of edit to delete
        """
        del self.edit_list[index]
