import random
from jmetal.core.operator import Mutation
from jmetal.util.ckecking import Check
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
        Check.that(type(solution) is QPatch, "Solution type invalid")

        lp = len(solution.edit_list)
        for j in range(lp):
            rand = random.random()
            if rand <= self.probability:
                rnd = random.random()
                if lp > 1 and rnd < 0.33:
                    if j < len(solution.edit_list):
                        solution.remove(j)
                    j -= 1
                    lp -= 1
                elif lp == 0 or rnd < 0.66:
                    edit_operator = random.choice(self.prg.operators)
                    solution.add(edit_operator.create(self.prg))
                else:
                    edit_operator = random.choice(self.prg.operators)
                    if j < len(solution.edit_list):
                        solution.edit_list[j] = edit_operator.create(self.prg)

        return solution
        return solution

    def get_name(self):
        return 'qGen Mutation'