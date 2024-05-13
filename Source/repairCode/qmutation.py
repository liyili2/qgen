import random
from jmetal.core.operator import Mutation
from .qpatch import QPatch

"""
.. module:: mutation
   :platform: Unix, Windows
   :synopsis: Module implementing mutation operators.

.. moduleauthor:: 
"""
class NullMutation(Mutation[QPatch]):
    """
    Null Mutation which does nothing
    """
    def __init__(self):
        super(NullMutation, self).__init__(probability=0)

    def execute(self, solution: QPatch) -> QPatch:
        return solution

    def get_name(self):
        return 'Null mutation'

class QMutation(Mutation[QPatch]):
    """
    Pyggi Mutation which changes the pyggi edit lists
    """
    def __init__(self):
        super(QMutation, self).__init__(probability=0)

    def execute(self, solution: QPatch) -> QPatch:
        """
        What Mutations:
        Add to edit list

        Remove from edit list

        Change order of edit list

        Change an item in the item list (remove and replace in same location)
        """
        return solution

    def get_name(self):
        return 'Pyggi mutation'