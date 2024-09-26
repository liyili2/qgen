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
    y.visitRoot(newTree)
    new_state = y.get_state()
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
            elif "num_qubits" in line:
                current_case['num_qubits'] = line.split(":")[1].strip()
            elif "array_size_na" in line:
                current_case['array_size_na'] = line.split(":")[1].strip()
            elif "initial_state_x" in line:
                current_case['initial_state_x'] = line.split(":")[1].strip()
            elif "input_value_m" in line:
                current_case['input_value_m'] = line.split(":")[1].strip()

        if current_case:
            test_cases.append(current_case)  # Append the last case

    return test_cases

# Mapping TSL inputs to actual values
def map_tsl_to_values(term, parameter_type):
    mappings = {
        'num_qubits': {
            'small': (2, 4),
            'medium': (4, 8),
            'large': (8, 16),
            'max': (16, 32),
            'one_bit': (1, 1)
        },
        'array_size_na': {
            'small': (1, 4),
            'medium': (5, 8),
            'large': (9, 16)
        },
        'input_value_m': {
            'small': (1, 10),
            'medium': (11, 100),
            'large': (101, 1000),
            'zero': (0, 0),
            'max_value': (10001, 65535)
        },
        'initial_state_x': {
            'zero_state': (0, 0),
            'max_state': (1 << 3, 1 << 4),
            'random_state': (1, 15)
        }
    }
    
    return mappings[parameter_type].get(term, (0,0))

# Save the mapped TSL values to a JSON file so they can be reused
def save_mapped_tsl_to_file(test_cases, output_file):
    mapped_test_cases = []

    for case in test_cases:
        mapped_case = {
            'num_qubits': random.randint(*map_tsl_to_values(case['num_qubits'], 'num_qubits')),
            'array_size_na': random.randint(*map_tsl_to_values(case['array_size_na'], 'array_size_na')),
            'initial_state_x': random.randint(*map_tsl_to_values(case['initial_state_x'], 'initial_state_x')),
            'input_value_m': random.randint(*map_tsl_to_values(case['input_value_m'], 'input_value_m'))
        }
        mapped_test_cases.append(mapped_case)

    # Save the mapped values to a JSON file
    with open(output_file, 'w') as f:
        json.dump(mapped_test_cases, f)

    print(f"Mapped TSL values saved to {output_file}")

# Load mapped values from JSON file
def load_mapped_tsl_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found. Ensure the values are saved first.")
    
    with open(file_path, 'r') as f:
        return json.load(f)

# Usage: First, parse and save the mapped TSL values to a JSON file
test_cases = parse_tsl_file("Benchmark/rz_adder/rz_adder.tsl.tsl")
save_mapped_tsl_to_file(test_cases, "Benchmark/rz_adder/mapped_tsl_values.txt")

# Load the mapped values from the JSON file
mapped_test_cases = load_mapped_tsl_from_file("Benchmark/rz_adder/mapped_tsl_values.txt")

# Generate pytest parameterization from the loaded values
@pytest.mark.parametrize("num_qubits, array_size_na, initial_state_x, input_value_m", [
    (case['num_qubits'], case['array_size_na'], case['initial_state_x'], case['input_value_m'])
    for case in mapped_test_cases
])
def test_basic_addition(num_qubits, array_size_na, initial_state_x, input_value_m):
    print("Test case:", num_qubits, array_size_na, initial_state_x, input_value_m)
    expected = ((initial_state_x) + (input_value_m % (2 ** array_size_na))) % 2 ** num_qubits
    assert run_rz_adder_test(num_qubits, array_size_na, initial_state_x, input_value_m) == expected

# Fixture to track the runtime of tests
@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
