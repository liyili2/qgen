import time
import pytest
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import CoqNVal, Simulator, bit_array_to_int, to_binary_arr


#def check_classification(triangles, expected_result):
#    for triangle in triangles:
 #       assert classify_triangle(*triangle) == expected_result


#def test_invalid_triangles():
 #   triangles = [(1, 2, 9), (1, 9, 2), (2, 1, 9), (2, 9, 1), (9, 1, 2),
     #            (9, 2, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
  #  check_classification(triangles, TriangleType.INVALID)


# test_equalateral_triangles():
  #  triangles = [(1, 1, 1), (100, 100, 100), (99, 99, 99)]
 #   check_classification(triangles, TriangleType.EQUALATERAL)


#def test_isoceles_triangles():
#    triangles = [(100, 90, 90), (90, 100, 90), (90, 90, 100), (3, 3, 2), (3, 2, 3), (2, 3, 3)]

#    check_classification(triangles, TriangleType.ISOCELES)


#def test_scalene_triangles():
#    triangles = [(5, 4, 3), (5, 3, 4), (4, 5, 3), (4, 3, 5), (3, 5, 4)]
#    check_classification(triangles, TriangleType.SCALENE)


# for the first step, the fitness is the percentage of correctness. How many test cases a program run correctly.
# the correctness is defined as array, x, y and c, the input is (x) with a constant m, and the output is (x+m)

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
    state = dict({"x": [CoqNVal(val_array, 0)], "na": num_qubits,
                  "m": addend})  # initial a chainMap having variable "x" to be 0 (list of False)
    environment = dict(
        {"x": num_qubits})  # env has the same variables as state, but here, variable is initiliazed to its qubit num
    y = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    y.visitProgram(tree)
    new_state = y.get_state()
    assert (110 == bit_array_to_int(new_state.get('x')[0].getBits(), num_qubits))


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)