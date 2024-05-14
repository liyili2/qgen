from pyggi.base.edit import AbstractEdit
from jmetal.core.problem import Problem
from .qpatch import QPatch
import random

class QProblem(Problem):
    """ Problem Q
            What is target description

    """

    def __init__(self,program, number_of_variables: int = 8):
        """
        :param number_of_variables: Number of decision variables of the problem.
        :param prg: Program object from pyggi
        """
        super(QProblem, self).__init__()
        self.program = program
        self.number_of_variables = 1
        self.number_of_objectives = 1
        self.obj_directions = [self.MINIMIZE]
        self.obj_labels = ['Fitness']

        self.number_of_constraints = 0

    def number_of_variables(self) -> int:
        return self.number_of_variables

    def number_of_objectives(self) -> int:
        return self.number_of_objectives

    def number_of_constraints(self) -> int:
        return self.number_of_constraints

    def evaluate(self, solution: QPatch) -> QPatch:
        fitness = self.program.evaluate_solution(solution, self.program.test_command)
        solution.fitness = fitness
        solution.objectives[0] = solution.fitness

        return solution

    def create_solution(self) -> QPatch:
        solution = QPatch(self.program, number_of_variables=1, number_of_objectives=1)
        edit_operator: AbstractEdit = random.choice(self.program.operators) 
        opr = edit_operator.create(self.program)
        solution.add(opr)
        return solution

    def generate_neighbor(self, solution: QPatch) -> QPatch:
        rnd = random.random()
        lp = len(solution)
        if lp == 0 or rnd < 0.33:
            edit_operator = random.choice(self.prg.operators)
            solution.add(edit_operator.create(self.prg))
        elif lp > 1 and rnd < 0.66:
            solution.remove(random.randrange(0, lp))
        else:
            edit_operator = random.choice(self.program.operators)
            pn = random.randrange(0, lp)
            solution.edit_list[pn] = edit_operator.create(self.prg)

        return solution

    def name(self):
        return 'QProblem'