import time
import pytest
import random
import json
import os
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import CoqNVal, Simulator, bit_array_to_int, to_binary_arr
from Source.quantumCode.AST_Scripts.ProgramTransformer import ProgramTransformer


# Test function to initialize and run the rz_adder simulation
def run_rz_adder_test(num_qubits, array_size_na, val, addend):
    with open("Benchmark/rz_adder/rz_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.root()
    transform = ProgramTransformer()
    newTree = transform.visitRoot(tree)
    
    val_array = to_binary_arr(val, num_qubits)  # Convert value to array
    state = dict({"x": [CoqNVal(val_array, 0)],
                  "size": num_qubits,
                  "na": array_size_na,
                  "m": addend})  # Initial state
    environment = dict({"x": num_qubits})  # Environment for simulation
    y = Simulator(state, environment)
    print(f"Initial state: {state}")
    y.visitRoot(newTree)
    new_state = y.get_state()
    print(f"new state: {new_state.get('x')[0].getBits()}")
    return bit_array_to_int(new_state.get('x')[0].getBits(), num_qubits)


# Function to parse TSL file
def parse_tsl_file(file_path):
    test_cases = []
    current_case = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Test Case"):
                if current_case:
                    test_cases.append(current_case)
                current_case = {}  # Reset current case for next one
            elif "size" in line:
                current_case['size'] = line.split(":")[1].strip()
            elif "na" in line:
                current_case['na'] = line.split(":")[1].strip()
            elif "x_input" in line:
                current_case['x_input'] = line.split(":")[1].strip()
            elif "input_value_m" in line:
                current_case['input_value_m'] = line.split(":")[1].strip()

        if current_case:
            test_cases.append(current_case)  # Append the last case

    return test_cases

# Mapping TSL inputs to actual values
def map_tsl_to_values(term, parameter_type):
    mappings = {
      'size': {  # Size of the qubit array
            'small': (1, 4),
            'medium': (4, 8),
            'large': (8, 16),
        },
        'na': {
            'small': (1, 4), # Small iteration range
            'medium': (5, 8),
            'large': (9, 16)
        },
        'input_value_m': {  # Natural number 'm' to be added in rz_adder
            'small': (1, 10),
            'medium': (11, 100),
            'large': (101, 1000),
            'zero': (0, 0),
            'max_value': (10001, 65535)
        },
        'x_input': {  # Initial state of the qubit array 'x'
            'zero_state': (0, 0),
            'random_state': (101, 1000),
            'max_state': (10001, 65535),
            
        }
    }
    
    return mappings[parameter_type].get(term, (0,0))

# Function to apply the constraint that 'na' should not exceed 'size'

def apply_constraints(mapped_case):
    # Ensure 'na' is less than or equal to 'size'
    if mapped_case['na'] > mapped_case['size']:
        mapped_case['na'] = random.randint(1, mapped_case['size'])
    
    return mapped_case
    

# Save the mapped TSL values to a JSON file so they can be reused
def save_mapped_tsl_to_file(test_cases, output_file):
     # If the file already exists, load it instead of generating new values
    if os.path.exists(output_file):
        print(f"Mapped TSL file {output_file} already exists. Loading existing values.")
        return
    mapped_test_cases = []

    for case in test_cases:
        mapped_case = {
            'size': random.randint(*map_tsl_to_values(case['size'], 'size')),
            'na': random.randint(*map_tsl_to_values(case['na'], 'na')),
            'x_input': random.randint(*map_tsl_to_values(case['x_input'], 'x_input')),
            'input_value_m': random.randint(*map_tsl_to_values(case['input_value_m'], 'input_value_m'))
        }
        mapped_case = apply_constraints(mapped_case)
        mapped_test_cases.append(mapped_case)

    # Save the mapped values to a JSON file
    with open(output_file, 'w') as f:
        json.dump(mapped_test_cases, f ,indent=4) 

    print(f"Mapped TSL values saved to {output_file}")

# Load mapped values from JSON file
def load_mapped_tsl_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found. Ensure the values are saved first.")
    
    with open(file_path, 'r') as f:
        return json.load(f)

# Usage: First, parse and save the mapped TSL values to a JSON file
test_cases = parse_tsl_file("Benchmark/rz_adder/rz_adder.tsl.tsl")
save_mapped_tsl_to_file(test_cases, "Benchmark/rz_adder/mapped_tsl_values.json")

# Load the mapped values from the JSON file
mapped_test_cases = load_mapped_tsl_from_file("Benchmark/rz_adder/mapped_tsl_values.json")

#Generate pytest parameterization from the loaded values
@pytest.mark.parametrize("size,na,x_input, input_value_m", [
    (case['size'], case['na'], case['x_input'], case['input_value_m'])
    for case in mapped_test_cases
])
def test_basic_addition(size, na ,x_input, input_value_m):
    expected = ((x_input) + (input_value_m % (2 ** na))) % 2 ** size
    assert run_rz_adder_test(size,na,x_input, input_value_m) == expected


  # Initial state

# Fixture to track the runtime of tests
@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
