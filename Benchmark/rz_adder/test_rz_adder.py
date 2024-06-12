import time
import pytest
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import CoqNVal, Simulator, bit_array_to_int, to_binary_arr


# Test function to initialize and run the rz_adder simulation
def run_rz_adder_test(num_qubits,val,addend):
    with open("rz_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    #print(tree.toStringTree(recog=parser))

    # num_qubits = 16  # Number of Qubits
    # val = 100  # init value
    # addend = 10
    val_array = to_binary_arr(val, num_qubits)  # conver value to array
    state = dict({"x": [CoqNVal(val_array, 0)],
                  "na": num_qubits,
                  "m": addend})  # initial a chainMap having variable "x" to be 0 (list of False)
    environment = dict(
        {"x": num_qubits})  # env has the same variables as state, but here, variable is initiliazed to its qubit num
    y = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    y.visitRoot(tree)
    new_state = y.get_state()
    return bit_array_to_int(new_state.get('x')[0].getBits(), num_qubits)

def test_basic_addition():
    assert (run_rz_adder_test(4, 5, 4) == 9)

def test_carry_propagation():
   assert run_rz_adder_test(4, 14, 3) == 1  # 1110 + 0011 = 10001 % 2^4 = 0001

def test_array_size_limit():
    assert run_rz_adder_test(4, 3, 13) == 0  # 0011 + 1101 = 10000 % 2^4 = 0000

def test_large_numbers():
    assert run_rz_adder_test(64, 2**32, 2**32) == 2**33  # 2^32 + 2^32 % 2^64 = 0

def test_zero_addend():
    assert run_rz_adder_test(16, 10, 0) == 10

def test_zero_qubit_array():
    assert run_rz_adder_test(16, 0, 5) == 5

@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
