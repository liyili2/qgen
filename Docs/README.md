
# Overview 

This project focuses on the genetic optimization of quantum programs using a combination of the Pyggi and jMetal libraries. The primary goal is to automatically improve quantum programs by applying genetic algorithms, which systematically explore and refine different configurations of the program to enhance performance, correctness, or other target metrics.

# Integration of Pyggi and jMetal in the Project:

In this project, Pyggi and jMetal work together to facilitate the genetic optimization of quantum programs.Pyggi provides the structure for representing quantum programs and the mechanisms for applying edits (mutations) to these programs. It handles the detailed manipulation of the program's code, enabling the genetic algorithm to explore different configurations.
jMetal provides the metaheuristic framework, driving the optimization process by defining the problem, generating and evaluating solutions, and applying genetic operators like mutation and crossover. jMetal manages the flow of the genetic algorithm, ensuring that the best-performing solutions are selected and refined over successive generations.

# Benchmarks 

The Benchmark folder in the project includes various subdirectories, each representing a different quantum program used as a test case for the genetic optimization process. These examples serve as the basis for evaluating how effectively the genetic algorithm can improve the performance or correctness of quantum programs. Each subdirectory contains the necessary files for defining, configuring, and testing a specific quantum program.

# Simulator 

The Simulator is responsible for executing the quantum circuits or programs generated by the genetic algorithm, allowing to evaluate their performance and correctness. The Simulator takes the quantum programs (often represented in XML format or as QPatch objects) and runs them within a simulated quantum environment. This execution mimics how the quantum circuit would behave on a real quantum computer, providing insights into the program's functionality.

# Modules 

# Qgen.py

The core logic starts by parsing command-line arguments using parser_generator().
Initializes a QProgram object with the provided project path and operators.
Encapsulates the quantum program within a QProblem object, defining the optimization task.
It selects and configures a genetic algorithm, typically GeneticAlgorithm from jMetalpy, with specified parameters like population size, mutation and crossover rates, and selection method. 
The algorithm iterates through generations, applying modifications to the program and evaluating their fitness. Upon completion, the script outputs the optimized program and a list of applied edits, providing a clear summary of the improvements made. 


# Qprogram.py

The QProgram class extends the TreeProgram class from the Pyggi framework. This module facilitates the management and optimization of quantum programs. Upon initialization, it reads and parses a quantum program from an XML file located in a specified directory. It maintains a list of modifiable operators that can alter the program. The module supports operations to select target modification points within the program, apply changes, and evaluate the impact of these changes.

Fitness evaluation is performed by executing the modified program and analyzing the test results. The module computes fitness based on the number of test failures and runtime metrics, adjusting the program accordingly. It also incorporates stopping criteria to determine when optimization should cease, typically when a satisfactory fitness level is achieved. The QProgram module thus plays a central role in evolving quantum programs by iteratively applying, testing, and refining changes to improve performance.

# Qproblem.py

The QProblem class is responsible for managing the core aspects of the optimization process. It initializes with a QProgram object, which represents the quantum program to be optimized, and sets the parameters for the optimization, such as the number of variables and objectives. The class provides a method for creating new solutions (QPatch objects) by applying random edit operators to the program, ensuring a diverse set of candidate solutions. During the evaluation phase, QProblem uses the evaluate_solution method to assess the fitness of each QPatch, typically by running the program against test cases in a simulator and computing a fitness score based on the results. This fitness score is crucial for determining how well a solution performs and guides the selection process in the genetic algorithm. Overall, QProblem serves as the interface between the quantum program and the genetic algorithm, enabling systematic exploration and optimization of the program's configuration.

# Qpatch.py

The QPatch class extends both the Solution class from jMetal and the Patch class from Pyggi, combining the functionalities needed to represent and manipulate a sequence of edits or modifications applied to a quantum program.This class stores a list of edits, each representing a change made to the original quantum program, such as inserting, deleting, or replacing quantum gates. When a QPatch is created, it initializes with an empty or pre-defined edit list, depending on the context of its creation. The class allows for easy addition, removal, and reordering of edits, facilitating the mutation and crossover operations that drive the exploration of the solution space.

# Crossover.py

The PyggiCrossover class implements the crossover operation for a genetic algorithm, combining two parent QPatch solutions to create new offspring solutions. This process involves swapping portions of the parents' edit lists to produce variations in the offspring. The class is initialized with a probability of performing the crossover and ensures that exactly two parents are used to generate two children.

Functionality 
Checks that there are exactly two parents.
Performs a deep copy of the parent solutions to avoid modifying the originals.
Determines the lengths of the parents' edit lists.
If either parent's edit list is empty, it simply combines their edit lists.
Otherwise, it performs a crossover at the midpoint of the edit lists, swapping the second halves of the parents' edit lists.
Returns two new QPatch offspring solutions created from the parents.

# Mutation.py

The Mutation module implements the mechanisms by which small, random changes are introduced to the solutions (QPatch objects) within the context of a genetic algorithm.Upon initialization, it takes a probability value that determines the likelihood of mutation for each edit in the QPatch. During execution, the class iterates over the edit list, randomly deciding whether to remove, add, or replace edits based on the mutation probability. By altering the sequence of edits, the mutation helps the algorithm explore different parts of the solution space, thereby preventing premature convergence on suboptimal solutions. The modified QPatch is then returned, ready for further evaluation or processing within the algorithm.

# Operators.py

The Operators module defines custom edit operations that can be applied to a quantum program within the genetic algorithm. These operations, such as insertion, replacement, and deletion of quantum gates, modify the structure of the quantum program represented by a QPatch. By using these operators, the genetic algorithm can generate a diverse set of candidate solutions, each representing a different configuration of the quantum program.The Operators module contains classes like QGateInsertion, QGateReplacement, and QGateDeletion, which provide specific mechanisms for modifying quantum programs:

QGateInsertion:
This operator allows the insertion of a new quantum gate at a specific location within the program. It selects a target point in the program where a new gate, derived from an existing ingredient or a random choice, can be inserted. The direction of insertion (before or after the target) can also be specified.

QGateReplacement:
This operator replaces an existing quantum gate in the program with another gate. It identifies the gate to be replaced and selects a suitable replacement from the available options, ensuring that the program's logic is altered in a meaningful way. This helps explore alternative program configurations by swapping critical operations.

QGateDeletion:
This operator removes a quantum gate from the program. By deleting specific gates, the operator simplifies the program, which may lead to discovering more efficient or functional configurations that were previously obscured by unnecessary operations.
