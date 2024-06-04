import time
import pytest
from antlr4 import InputStream, CommonTokenStream

# for the first step, the fitness is the percentage of correctness. How many test cases a program run correctly.
# the correctness is defined as array, x, y and c, the input is (x) with a constant m, and the output is (x+m)
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import Coq_nval, Simulator, calInt, to_binary_arr


def test_init():
    with open("Benchmark/rz_adder/rz_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    num_qubits = 16  # Number of Qubits
    val = 100  # init value
    addend = 10
    val_array = to_binary_arr(val, num_qubits)  # conver value to array
    state = dict({"x": Coq_nval(val_array, 0), "na": num_qubits,
                  "m": addend,
                  "M": 0})  # initial a chainMap having variable "x" to be 0 (list of False)
    environment = dict(
        {"x": num_qubits})  # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    assert (110 == calInt(new_state.get('x').getBits(), num_qubits))


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
