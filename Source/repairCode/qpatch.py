"""
This module contains Patch class.
"""
from jmetal.core.solution import Solution
from pyggi.base.patch import Patch
from pyggi.base.edit import AbstractEdit

class QPatch(Solution,Patch):
    """
    Modified Patch to work with jMetal
    Adds the pyggi edit list 
    """
    def __init__(self, program, number_of_variables: int = 1, number_of_objectives: int = 1):
        """
        Modify this if additonal state needed
        """
        # Intialize the jMetal Solution Object
        super(QPatch, self).__init__(number_of_variables=number_of_variables, number_of_objectives=number_of_objectives)
        # Support the pyggi edit lists
        self.program = program
        self.edit_list = []   
        self.objectives = [1]
        # TODO # Initialize to infinity / large number
        self.objectives[0] = 10000
        print("I made a qPacth")

    # Sort according fitness in decreasing order
    def __lt__(self, other):
        '''
        Compare two qPatches
        '''
        if self.fitness is None: return False
        if other.fitness is None: return True

        # Checking edit list length if tied
        #if abs(self.fitness - other.fitness) < PRECISION:
        #    return self.__len__() < other.__len__()

        return self.fitness < other.fitness

    def __repr__(self):
        '''
        ???
        '''
        return '\n'.join(list(map(str, self.edit_list)))

    def __len__(self):
        '''
        Length of the edit list
        '''
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
