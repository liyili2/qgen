import time
import pytest
from antlr4 import InputStream, CommonTokenStream

# from Benchmark.Triangle.triangle import TriangleType, classify_triangle # this might not be correct
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import calBin, Coq_nval, Simulator, calInt

# for the first step, the fitness is the percentage of correctness. How many test cases a program run correctly.
# the correctness is defined as array, x, y and c, the input is (x,y,c), and the output is (x,x+y,c)

def test_init():
    # //We first turn x array to QFT type, and we apply SR gate to rotate the phase of x for 2 pi i * (1/2^10). It will make sense if 10 < rmax, RQFT is the inverse of QFT.
    with open("Benchmark/cl_adder/cl_adder.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    # the following shows an example of using 1 variable state. You can have a 10 variable state
    # see that a variable is a string.
    num = 16  # Number of Qubits
    val = 100  # init value
    valArray = calBin(val, num)  # conver value to array
    # val = [False]*num # state for x
    state = dict(
        {"x": Coq_nval(valArray, 0), "M": val})  # initial a chainMap having variable "x" to be 0 (list of False)
    environment = dict(
        {"x": num})  # env has the same variables as state, but here, variable is initiliazed to its qubit num
    y = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    y.visitProgram(tree)
    newState = y.get_state()
    assert (132 == calInt(newState.get('x').getBits(), num))

    # Do assertion check that state is as expected
    # Add function to do state (binary-> int ) conversion  #TODO#
    # int n = calInt(arrayQuBits, sizeArray)
    # assert newState == state

@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
