import time
import pytest
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import CoqNVal, Simulator, bit_array_to_int, to_binary_arr


# for the first step, the fitness is the percentage of correctness. How many test cases a program run correctly.
# the correctness is defined as array, x, y and c, the input is (x) with a constant m, and the output is (x+m)

def simulate_qubit_adder(num_qubits, val_qubit, addend):
    with open("Benchmark/rz_adder/rz_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    val_binary_array = to_binary_arr(val_qubit, num_qubits)  # conver value to array
    state = dict({"x": [CoqNVal(val_binary_array, 0)],
                  "na": num_qubits,
                  "m": addend})  # initial a chainMap having variable "x" to be 0 (list of False)
    environment = dict(
        {"x": num_qubits})  # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    return new_state


def check_rz_adder_result(new_state, expected_result, num_qubits):
    final_x_value = bit_array_to_int(new_state.get('x')[0].getBits(), num_qubits)
    assert final_x_value == expected_result, \
        f"Expected {expected_result}, Final {final_x_value}"


def test_rz_adder():
    test_cases = [
        {"num_qubits": 16, "val_x": 22, "val_m": 971, "expected_result": 993, "description": "Small Even, Large Odd"},
        {"num_qubits": 16, "val_x": 150, "val_m": 25, "expected_result": 175, "description": "Medium Even, Small Odd"},
        {"num_qubits": 16, "val_x": 999, "val_m": 1025, "expected_result": 2024, "description": "Large Odd, Medium Odd"},
        {"num_qubits": 16, "val_x": 0, "val_m": 1, "expected_result": 1, "description": "Small Even, Small Odd"},
        {"num_qubits": 16, "val_x": 500, "val_m": 501, "expected_result": 1001, "description": "Medium Even, Medium Odd"},
    ]

    for case in test_cases:
        new_state = simulate_qubit_adder(case["num_qubits"], case["val_x"], case["val_m"])
        check_rz_adder_result(new_state, case["expected_result"], case["num_qubits"])


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
