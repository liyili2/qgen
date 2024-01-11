from quantumCode.AST_Scripts.XMLVisitor import XMLVisitor
from quantumCode.simulator import Simulator
from repairCode.crossover import QCrossover
from repairCode.mutation import QMutation
from repairCode.patch import QPatch
from repairCode.problem import QProblem

from pyggi.base import AbstractProgram
from pyggi.algorithms import GA
from pyggi.atomic import Mutation, Crossover
from pyggi.utils import Logging

def main():
    # File path to the quantum program
    quantum_program_path = 'path/quantum_program.py'

    with open(quantum_program_path, 'r') as file:
        source_code = quantum_program_path.read()

    # Generate solutions
    problem_instance = QProblem(source_code)

    # Define genetic operators
    mutation = Mutation(problem_instance, QMutation())
    crossover = Crossover(problem_instance, QCrossover())

    # Define the genetic algorithm
    algorithm = GA(problem_instance, mutation=mutation, crossover=crossover)

    logging = Logging(problem_instance)

    # Run the genetic improvement process
    algorithm.run(logging=logging)

    best_solution = algorithm.best

    # Retrieve the best quantum program
    best_program = best_solution.to_real()
    print(best_program)

if __name__ == "__main__":
    main()
