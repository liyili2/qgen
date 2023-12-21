import random
from jmetal.core.operator import Mutation
from jmetal.util.ckecking import Check
from tools.hypergi import ProgramEntropy
from tools.jppatch import JPPatch

"""
.. module:: mutation
   :platform: Unix, Windows
   :synopsis: Module implementing mutation operators.

.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>, Antonio Benítez-Hidalgo <antonio.b@uma.es>
"""


class QMutation(Mutation[JPPatch]):

    def __init__(self, probability: float, prg: QProgram):
        super(QMutation, self).__init__(probability=probability)
        self.prg = prg

    def execute(self, solution: QPatch) -> QPatch:
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

    def get_name(self):
        return 'QMutation'
