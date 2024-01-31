from quantumCode.AST_Scripts.XMLVisitor import XMLVisitor
# from quantumCode.simulator import Simulator
from repairCode.crossover import QCrossover
from repairCode.mutation import QMutation
from repairCode.patch import QPatch
from repairCode.problem import QProblem

from pyggi.base import AbstractProgram
# from pyggi.algorithms import GA
# from pyggi.atomic import Mutation, Crossover
# from pyggi.utils import Logging

from jmetal.core.operator import Mutation
from jmetal.operator.crossover import Crossover

import unittest
from antlr4 import *
from quantumCode.AST_Scripts.ExpListener import ExpListener
from quantumCode.AST_Scripts.ExpLexer import ExpLexer
from quantumCode.AST_Scripts.ExpParser import ExpParser
from quantumCode.AST_Scripts.XMLVisitor import XMLVisitor

from argparse import ArgumentParser


def main(args):
    # File path to the quantum program
    # quantum_program_path = 'path/quantum_program.py'

    # with open(quantum_program_path, 'r') as file:
    #     source_code = quantum_program_path.read()

    # Generate solutions
    i_stream = InputStream("X (x,0) ; CU (x,0) (CU (x,1) (X (y,1)))")
    lexer = ExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = ExpParser(t_stream)
    tree = parser.program()
    xml = XMLVisitor()
    problem_instance = tree.accept(xml)

    # Define genetic operators
    mutation = Mutation(problem_instance, QMutation())
    crossover = Crossover(problem_instance, QCrossover())

    # Define the genetic algorithm
    algorithm = GA(problem_instance, mutation=mutation, crossover=crossover)
    # Add if conditionals for other algorithims

    #
    logging = Logging(problem_instance)

    # Run the genetic improvement process
    algorithm.run(logging=logging)

    best_solution = algorithm.best

    # Retrieve the best quantum program
    best_program = best_solution.to_real()
    print(best_program)


if __name__ == "__main__":
    """ 
    Default tags to keep in AST, 
    Because the program is expected to provide sbml output, this tools keeps all the tags
    """
    algorithms = ['GA', 'SA', 'RS', 'NSGAII']
    default_tags = "listOfReactants reaction reactants species rate products listOfParameters "
    default_tags += "annotation SimBiology Version model listOfCompartments compartment "
    default_tags += "speciesReference listOfProducts kineticLaw math apply ci times parameter"
    algo = algorithms[0]
    epochs = 2
    iter = 100
    pop = 10

    """ 
    Below are the list of command-line (Program) parameters that can be 
        received during a run.
    If a command-line parameter is not provided, the default 
        value given below will be used.
    """
    parser = ArgumentParser(description='PyGGI CRN Repair Example')
    parser.add_argument('--project_path', type=str, default='sample/crn-framework')
    parser.add_argument('--matlab1', type=str, default='matlab')
    parser.add_argument('--algo', type=str, default=algo)
    parser.add_argument('--subject', type=str, default="H1")
    parser.add_argument('--model', type=str, default="101")
    parser.add_argument('--somo', type=str, default="SO")
    parser.add_argument('--tags', type=str, default=default_tags)
    parser.add_argument('--mmo_wgh', type=float, default=1, help='MMO weight')
    parser.add_argument('--target', type=float, default=0, help='Target Fitness')
    parser.add_argument('--probs', type=int, default=0,
                        help='1: Use localization probabilities; 0: Random')
    parser.add_argument('--new_reaction', type=int, default=1,
                        help="1: Use new reaction operator")
    parser.add_argument('--pop', type=int, default=pop, help='Population for GA')
    parser.add_argument('--jobid', type=str, default='0')
    parser.add_argument('--load_mutations', type=str, default='False')
    parser.add_argument('--operationTags', type=str, default="speciesReference reaction")  #
    parser.add_argument('--engine', type=bool, default=True)
    parser.add_argument('--mutation', type=float, default=0.9)
    parser.add_argument('--crossover', type=float, default=0.9)
    parser.add_argument('--nspec', type=int, default=2,
                        help='Number of ingredients')
    parser.add_argument('--timeout', type=float, default=8,
                        help='time to force-terminate programs if they don\'t end regularly')
    parser.add_argument('--epochs', type=int, default=epochs,
                        help='total epoch(default: 10)')
    parser.add_argument('--iter', type=int, default=iter,
                        help='Generations or iterations per epoch')
    parser.add_argument('--debug', type=int, default=0,
                        help='In debug mode (1) or or not (0)')

    arg_prs = parser.parse_args()
    arg_prs.somo = "MMO"
    if arg_prs.algo in ["GA", "SA", "RS"]:
        arg_prs.somo = "SO"

    main(arg_prs)
