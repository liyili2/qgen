"""
This module contains Patch class.
"""
# import os
# from copy import deepcopy
#from constants import PRECISION, INF
from jmetal.core.solution import Solution
from pyggi.base.patch import Patch
from pyggi.base.edit import AbstractEdit

class PyggiPatch(Solution,Patch):
    """
    Modified Patch to work with jMetal
    Adds the pyggi edit list 
    """
    def __init__(self, program, number_of_variables: int = 1, number_of_objectives: int = 1):
        """
        Modify this if additonal state needed
        """
        # Intialize the jMetal Solution Object
        super(PyggiPatch, self).__init__(number_of_variables=number_of_variables, number_of_objectives=number_of_objectives)
        # Support the pyggi edit lists
        self.program = program
        self.edit_list = []   
        self.objectives = [1]
        print("I made a pyggiPath")

    def add(self, edit, after: bool = False):
            assert isinstance(edit, AbstractEdit)
 
            if after:
                     self.edit_list.append(edit)
            return
            self.edit_list.insert(0, edit)

class PPatch(PyggiPatch):
    """
    Modified PyggiPatch to work with Python Programs
    """
    pass

class QPatch(PyggiPatch):
    """
    Modified PyggiPatch to work with Quantum Programs
    """
    pass