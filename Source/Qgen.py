"""
Automated program repair ::
"""
import argparse

# For pyggi default program + repair
from pyggi.tree import XmlEngine
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion # Default Python program support
# From jMetalpy
from jmetal.algorithm.singleobjective import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.core.quality_indicator import FitnessValue, QualityIndicator
# For modified program + repair
from repairCode.qprogram import QProgram
from repairCode.qproblem import QProblem
from repairCode.qpatch import QPatch
from repairCode.qmutation import NullMutation, QMutation
from repairCode.qcrossover import QCrossover
from repairCode.operators import QGateReplacement, QGateInsertion, QGateDeletion

class MyXmlEngine(XmlEngine):
    """
    PyGGI uses its own engine. Then, it allows customizing some
    functionalities of engine classes through the use of subclasses.
    Subclass for XmlEngine
    """

    @classmethod
    def process_tree(cls, tree, tags):
        """
        Not used!!
        process_tree is used to customize AST for PyGGI
           select_tags removes all tags which are not in the tags list        
        """
        stmt_tags = tags
        cls.select_tags(tree, keep=stmt_tags)
        cls.rotate_newlines(tree)

if __name__ == "__main__":
    print("Starting")
    parser = argparse.ArgumentParser(description='PYGGI Bug Repair Example')
    parser.add_argument('--project_path', type=str, default='Benchmark/Triangle')
    parser.add_argument('--mode', type=str, default='ga')
    parser.add_argument('--epoch', type=int, default=1, help='total epoch(default: 1)')
    parser.add_argument('--iter', type=int, default=10, help='total iterations per epoch(default: 100)')
    parser.add_argument('--pop', type=int, default=8, help='population size(default: 10)')
    parser.add_argument('--mut', type=float, default=0, help='mutation rate(default: 0.1)')
    parser.add_argument('--cross', type=float, default=0, help='crossover rate(default: 0.9)')
    parser.add_argument('--sel', type=str, default='tournament', help='selection operator(default: tournament)')
    parser.add_argument('--tags', type=str, default='[]', help='XML tags (default: [])')
    args = parser.parse_args()

    # Make a Program
    program = QProgram(args.project_path)
    program.operators = [StmtDeletion, StmtInsertion, StmtReplacement]
    program.tags = args.tags
    # Make a Problem
    problem = QProblem(program, number_of_variables=8)
    # Choose which algorithm
    if args.mode == 'ga':
        ga = GeneticAlgorithm(problem, 2, 2,QMutation(0),QCrossover(0))
        ga.selection_operator    = BinaryTournamentSelection()
        ga.termination_criterion = StoppingByEvaluations(max_evaluations=args.iter)
        ga.run()
        result = ga.result()       
    # Add other algorithms here


    print("======================RESULT======================")
    print(result)
    #program.remove_tmp_variant()
