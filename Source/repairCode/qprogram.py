from pyggi.tree import TreeProgram

import re

from pyggi.base.program import RunResult

class QProgram(TreeProgram):
    """
    A Program 
    """

    def __init__(self, project_path):
        """
        :param number_of_variables: Number of decision variables of the problem.
        :param prg: Program object from pyggi
        """
        super(TreeProgram, self).__init__(project_path)
        self.path      = project_path
        self.operators = []

    def compute_fitness(self, result, return_code=0, stdout=0, stderr=0, elapsed_time=0):
        """
        Given a program, compute the fitness by parsing the pyTest output
        """
        print('start computing fitness')
        m = re.findall("runtime: ([0-9.]+)", stdout)
        print(f'Runtime: {m}')
        if len(m) > 0:
            runtime = m[0]
            failed_list = re.findall("([0-9]+) failed", stdout)
            if len(failed_list) > 0: 
                failed = int(failed_list[0])
            else: 
                failed = 0
            passed_list = re.findall("([0-9]+) passed", stdout)
            if len(failed_list) > 0: 
                passed = int(passed_list[0])
            else: 
                passed = 0
            total_tests = failed + passed
        
            result.fitness = failed
            #result.fitness = passed / total_tests if total_tests > 0 else 0
            print(f'Fitness: {result.fitness}')
        else:
            result.status = 'PARSE_ERROR'

        return result
        
    def stopping_criterion(self, iters, fitness):
        return fitness <= self.BEST
    
    def name(self) -> str:
        return "QProgram"
    
    # jMetal required functions

        
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