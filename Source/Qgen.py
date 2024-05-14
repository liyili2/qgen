"""
Automated program repair ::
"""
import argparse

# For pyggi default program + repair
from pyggi.tree import XmlEngine
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
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
    parser.add_argument('--project_path', type=str, default='../Benchmark/vqo_small_circuit_ex')
    parser.add_argument('--mode', type=str, default='ga')
    parser.add_argument('--epoch', type=int, default=1, help='total epoch(default: 1)')
    parser.add_argument('--iter', type=int, default=100, help='total iterations per epoch(default: 100)')
    args = parser.parse_args()
    #assert args.mode in ['line', 'tree']

    # Choose which algorithm
    if args.mode == 'ga':
        program = QProgram(args.project_path)
        program.operators = [StmtDeletion, StmtInsertion, StmtReplacement]
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
