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
        :param program: Program object from pyggi
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
        result = self.program.evaluate_solution(solution, self.program.test_command)
        # Check if result is valid # TODO #
        solution.objectives[0] = result.fitness

        return solution

    def create_solution(self) -> QPatch:
        solution = QPatch(self.program, number_of_variables=1, number_of_objectives=1)
        edit_operator: AbstractEdit = random.choice(self.program.operators) 
        opr = edit_operator.create(self.program)
        solution.add(opr)
        return solution

    def generate_neighbor(self, solution: QPatch) -> QPatch:
        rnd = random.random()
        edit_list_length = len(solution.edit_list)
        # If edit list is emoty or 1/3rd chance : Add
        if edit_list_length == 0 or rnd < 0.33:
            edit_operator = random.choice(self.program.operators)
            solution.add(edit_operator.create(self.program))
        # If more than one item in the edit list and 1/3rd chance : Remove
        elif edit_list_length > 1 and rnd < 0.66:
            solution.remove(random.randrange(0, edit_list_length))
        # Else, 1/3rd chance : Change
        else:
            edit_operator = random.choice(self.program.operators)
            edit_list_index = random.randrange(0, edit_list_length)
            solution.edit_list[edit_list_index] = edit_operator.create(self.program)

        return solution

    def name(self):
        return 'QProblem'