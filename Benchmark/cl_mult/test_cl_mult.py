import time
import pytest
from antlr4 import InputStream, CommonTokenStream

# from Benchmark.Triangle.triangle import TriangleType, classify_triangle # this might not be correct
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import to_binary_arr, CoqNVal, Simulator, bit_array_to_int


def test_full_cl_mult():
    with open("Benchmark/cl_mult/cl_mult_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    na = 16

    val_x = 2
    val_array_x = to_binary_arr(val_x, na)

    val_y = 10
    val_array_y = to_binary_arr(val_y, na)

    val_ca = 0
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)

    val_result = 0
    val_array_result = to_binary_arr(val_result, na)

    state = dict(
        {"xa": [CoqNVal(val_array_x, 0)],
         "ya": [CoqNVal(val_array_y, 0)],
         "ca": [CoqNVal(val_array_ca, 0)],
         "result": [CoqNVal(val_array_result, 0)],
         "na": na,
         })
    environment = dict(
        {"xa": na,
         "ya": na,
         "ca": num_qubits_ca,
         "result": na,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    assert (20 == bit_array_to_int(new_state.get('result')[0].getBits(), na))


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
