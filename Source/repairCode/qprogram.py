import random
from pyggi.tree import TreeProgram
from .qresult import QResult

import re


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
        #print('start computing fitness')
        m = re.findall("runtime: ([0-9.]+)", stdout)
        #print("stdout",stdout)
        #m = re.findall("runtime: (\d+\.\d+)s", stdout)
        print(f'Runtime: {m}')
        if len(m) > 0:
            runtime = m[0]
            failed_list = re.findall("([0-9]+) failed", stdout)
            if len(failed_list) > 0: 
                failed = int(failed_list[0])
            else: 
                failed = 0
            passed_list = re.findall("([0-9]+) passed", stdout)
            if len(passed_list) > 0: 
                passed = int(passed_list[0])
            else: 
                passed = 0
            total_tests = failed + passed
        
            result.fitness = failed
            #result.fitness = passed / total_tests if total_tests > 0 else 0
            #print(f'Fitness: {result.fitness}')
        else:
            result.status  = 'PARSE_ERROR'
            result.fitness = 1000000 # Large Value
        # Print Fitness
        print(f'Status: {result.status}')
        print(f'Fitness: {result.fitness}')
        return result


    def stopping_criterion(self, iters, fitness):
        return fitness <= self.BEST
    
    def name(self) -> str:
        return "QProgram"
    
    def app_target(self, target_file=None, method="random"):
        '''
        Similar to random target but tuned for app insertation


        '''
        if target_file is None:
            target_file = target_file or random.choice(self.target_files)
        assert target_file in self.target_files

        ## ADD CODE HERE
        valid_path_regex = re.compile(r'\./let\[1\]/match\[1\]/pair\[\d+\](/pexp|/if|/app)')
        candidates =[point for point in self.modification_points[target_file] if valid_path_regex.match(point)]
        
        assert method in ['random','weighted']

        if method == 'random' or target_file not in self.modification_weights:
            return (target_file,random.randrange(len(candidates)))

    # jMetal required functions

        
    def evaluate_solution(self, patch, test_command):
        '''
        Apply the edit list to the program and run the test command (pyTest)
        '''
        self.apply(patch)
        # print(patch, "\n")
        # return_code is the return code of the program execution
        tout = 10
        rcode, stdout, stderr, elapsed = self.exec_cmd(test_command, timeout=tout)
        result = QResult('SUCCESS', None)
        self.compute_fitness(result, rcode, stdout, stderr, elapsed)
        #print("=== STDOUT ===")
        #print(stdout)
        # print("=== STDERR ===")
        # print(stderr)
        return result
