from jmetal.core.problem import Problem
from jmetal.core.solution import Solution
from Source.repairCode.patch import QPatch
from pyggi.base.edit import AbstractEdit
from pyggi.tree import XmlEngine
import random


class QProblem(Problem[QPatch]):
    """ Problem Q
            What is target description

    """

    def __init__(self, prg: QProgram, number_of_variables: int = 8):
        """
        :param number_of_variables: Number of decision variables of the problem.
        :param prg: Program object from pyggi
        """
        super(QProblem, self).__init__()
        self.prg = prg
        self.number_of_variables = 1
        self.number_of_objectives = 1
        self.obj_directions = [self.MINIMIZE]
        self.obj_labels = ['Fitness']
        if prg.args.somo == "MO":
            self.number_of_objectives = 2
            self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
            self.obj_labels = ['?', 'Fail rate']

        self.number_of_constraints = 0

    def number_of_variables(self) -> int:
        return self.number_of_variables

    def number_of_objectives(self) -> int:
        return self.number_of_objectives

    def number_of_constraints(self) -> int:
        return self.number_of_constraints

    def evaluate(self, solution: JPPatch) -> JPPatch:
        fitness = self.prg.evaluate_solution(solution, self.prg.build_command)
        solution.fitness = entropy / 2 + f_rate / 2
        solution.objectives[0] = solution.fitness

        return solution

    def create_solution(self) -> Solution:
        no = 1
        if self.prg.args.somo == "MO":
            no = 2
        solution = QPatch(self.prg, number_of_variables=1, number_of_objectives=no)
        edit_operator: AbstractEdit = random.choice(self.prg.operators)
        if edit_operator in [NewIf, NewFor]:
            opr = edit_operator.create(self.prg)
        else:
            opr = edit_operator.create(self.prg)
        solution.add(opr)

        return solution

    def generate_neighbor(self, solution: QPatch) -> Solution:
        rnd = random.random()
        lp = len(solution)
        if lp == 0 or rnd < 0.33:
            edit_operator = random.choice(self.prg.operators)
            solution.add(edit_operator.create(self.prg))
        elif lp > 1 and rnd < 0.66:
            solution.remove(random.randrange(0, lp))
        else:
            edit_operator = random.choice(self.prg.operators)
            pn = random.randrange(0, lp)
            solution.edit_list[pn] = edit_operator.create(self.prg)

        return solution

    def name(self):
        return 'QuantumProblem'