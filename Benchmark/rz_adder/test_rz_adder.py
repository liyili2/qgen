import time
import pytest
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import  Coq_nval, Simulator, calInt,to_binary_arr


# Test function to initialize and run the rz_adder simulation
def test_init(x,na,m):
    # Read the rz_adder XML file
    with open("Benchmark/rz_adder/rz_adder_good.xml", 'r') as f:
        str = f.read()
    # Create an input stream from the read XML content
    i_stream = InputStream(str)
    # Initialize the lexer with the input stream
    lexer = XMLExpLexer(i_stream)
    # Create a token stream from the lexer output
    t_stream = CommonTokenStream(lexer)
    # Initialize the parser with the token stream
    parser = XMLExpParser(t_stream)
    # Parse the input to create a parse tree
    tree = parser.program()
    # Print the parse tree (for debugging purposes)
    print(tree.toStringTree(recog=parser))

    # # Initial test parameters
    #convert values to binary array

    valArray_x = to_binary_arr(x ,na) 
    valArray_y = to_binary_arr(m,na)
    state = dict({"x" : Coq_nval(valArray_x,0), 
                  "m" : Coq_nval(valArray_y,0),
                  "na": na}) #initial a chainMap having variable "x" to be 0 (list of False)
    environment = {
        "x" : na,
        "m" : na
        } #env has the same variables as state, but here, variable is initiliazed to its qubit num
    y = Simulator(state, environment) # Environment is same, initial state varies by pyTest
    y.visitProgram(tree)
    newState = y.get_state()
    return newState
    #assert(200 == calInt(newState.get('x').getBits(), na))

# Helper function to check the result
def check_rz_adder_result(new_state, expected_result, num_qubits):
    final_x_value = calInt(new_state.get('x').getBits(), num_qubits)
    assert final_x_value == expected_result, \
        f"Expected {expected_result}, Final {final_x_value}"

def test_rz_adder():
    test_cases = [
        {"num_qubits": 16, "val_x": 22, "val_M": 971, "expected_result": 993, "description": "Small Even, Large Odd"},
        {"num_qubits": 16, "val_x": 150, "val_M": 25, "expected_result": 175, "description": "Medium Even, Small Odd"},
        {"num_qubits": 16, "val_x": 999, "val_M": 1025, "expected_result": 2024, "description": "Large Odd, Medium Odd"},
        {"num_qubits": 16, "val_x": 0, "val_M": 1, "expected_result": 1, "description": "Small Even, Small Odd"},
        {"num_qubits": 16, "val_x": 500, "val_M": 501, "expected_result": 1001, "description": "Medium Even, Medium Odd"},
    ]

    for case in test_cases:
        new_state = test_init(case["num_qubits"], case["val_x"], case["val_M"])
        check_rz_adder_result(new_state, case["expected_result"], case["num_qubits"])


# Fixture to measure runtime
@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)

# Run the tests
if __name__ == "__main__":
    pytest.main()

