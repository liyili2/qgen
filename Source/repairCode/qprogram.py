
from jmetal.core.solution import Solution
from .qpatch import QPatch
from pyggi.line import LineProgram
from pyggi.tree import TreeProgram,StmtInsertion
from pyggi.base.program import RunResult
from pyggi.base.edit import AbstractEdit
from pyggi.tree import XmlEngine
from typing import Generic, TypeVar, List
import random
import re

class QProgram(TreeProgram):
    """
    
    """
    number_of_variables = 1
    number_of_objectives = 1
    number_of_constraints = 0

    def __init__(self, project_path):
        """
        :param number_of_variables: Number of decision variables of the problem.
        :param prg: Program object from pyggi
        """
        super(TreeProgram, self).__init__(project_path)
        self.path                  = project_path
        self.number_of_variables   = 1
        self.number_of_objectives  = 1
        self.number_of_constraints = 0
        self.obj_directions        = [self.MINIMIZE]
        self.obj_labels            = ['Fitness']
        

    def compute_fitness(self, result, return_code=0, stdout=0, stderr=0, elapsed_time=0):
        """
        Given a program, compute the fitness
        """
        print('start computing fitness')
        m = re.findall("runtime: ([0-9.]+)", stdout)
        print(f'm: {m}')
        if len(m) > 0:
            runtime = m[0]
            failed = re.findall("([0-9]+) failed", stdout)
            passed = re.findall("([0-9]+) passed", stdout)
            total_tests = failed + passed
        
            result.fitness = passed / total_tests if total_tests > 0 else 0
            print(f'result fitness: {result.fitness}')
        else:
            result.status = 'PARSE_ERROR'

        return result
        

    #def get_engine(cls, file_name=""):
    #   return MyXmlEngine

    # jMetalpy functions        
    def create_solution(self) -> QPatch:
        new_solution = QPatch(self, number_of_variables=1, number_of_objectives=1)
        return new_solution


    
    def evaluate_solution(self, patch, test_command):
        '''
        apply + run
        '''
        self.apply(patch)
        # rcode is the return code of the program execution
        # etime is the elapsed time of the program execution
        tout = 10
        rcode, stdout, stderr, elapsed = self.exec_cmd(test_command, timeout=tout)
        result = RunResult('SUCCESS', None)
        # result, return_code, stdout, stderr, elapsed_time, cov=0
        print(stdout)
        self.compute_fitness(result, rcode, stdout, stderr, elapsed)
        # print(result.status, result.leak)
        # assert (result.status == 'SUCCESS' and not (result.leak is None))
 
        return result

    def number_of_variables(self) -> int:
        return self.number_of_variables

    
    def number_of_objectives(self) -> int:
        return self.number_of_objectives

    def number_of_constraints(self) -> int:
        return self.number_of_constraints
    
    def name(self) -> str:
        return "MyProgram"

'''    def evaluate_patch(self, patch, timeout=15):
        # apply + run
        self.apply(patch)
        return_code, stdout, stderr, elapsed_time = self.exec_cmd(self.test_command, timeout)
        if return_code is None: # timeout
            return RunResult('TIMEOUT')
        else:
            result = RunResult('SUCCESS', None)
            self.compute_fitness(result, return_code, stdout, stderr, elapsed_time)
            assert not (result.status == 'SUCCESS' and result.fitness is None)
            return result
'''