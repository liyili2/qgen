"""
Automated program repair ::
"""
import sys
import os
import random
import argparse

# For pyggi default program + repair
from pyggi.line import LineReplacement, LineInsertion, LineDeletion
from pyggi.tree import XmlEngine
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
from pyggi.algorithms import LocalSearch
# For modified program + repair
from Source.repairCode.qFitness import QFitness
from Source.repairCode.qcrossover import PyggiCrossover, QCrossover
from Source.repairCode.qproblem import QProblem
from Source.repairCode.qmutation import NullMutation
from Source.repairCode.qpatch import PyggiPatch
from repairCode.operators import QGateReplacement, QGateInsertion, QGateDeletion
from Source.repairCode.qprogram import MyLineProgram, MyTreeProgram, MyProgram,PyggiProblem, QProgram
from jmetal.algorithm.singleobjective import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.core.quality_indicator import FitnessValue, QualityIndicator
from jmetal.core.solution import Solution

import os

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
    parser.add_argument('--project_path', type=str, default='Benchmark/vqo_small_circuit_ex')
    parser.add_argument('--mode', type=str, default='ga')
    parser.add_argument('--epoch', type=int, default=1, help='total epoch(default: 1)')
    parser.add_argument('--iter', type=int, default=100, help='total iterations per epoch(default: 100)')
    args = parser.parse_args()
    #assert args.mode in ['line', 'tree']

    # Choose which algorithm
    if args.mode == 'ga':
        program = QProgram(args.project_path)
        problem = QProblem(program, number_of_variables=8)
        ga = GeneticAlgorithm(problem, 8, 8, NullMutation(), QCrossover(.5))
        ga.selection = BinaryTournamentSelection()
        ga.operators = [QGateReplacement]
        ga.termination_criterion = StoppingByEvaluations(max_evaluations=args.iter)
        ga.run()
        result = ga.result()       
    
    print("======================RESULT======================")
    print(result)
    #program.remove_tmp_variant()
