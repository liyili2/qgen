import time
import pytest
from antlr4 import InputStream, CommonTokenStream

# from Benchmark.Triangle.triangle import TriangleType, classify_triangle # this might not be correct
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import to_binary_arr, CoqNVal, Simulator, bit_array_to_int


def test_full_rz_mod_div():
    with open("Benchmark/rz_mod_div/rz_mod_div_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    na = 40

    val_x = 10
    val_array_x = to_binary_arr(val_x, na)

    val_ex = 10
    val_array_ex = to_binary_arr(val_ex, na)

    modulo = 4

    i = 20

    state = dict(
        {"x": CoqNVal(val_array_x, 0),
         "ex": CoqNVal(val_array_ex, 0),
         "na": na,
         "modulo": modulo,
         "i": i,
         })
    environment = dict(
        {"x": na,
         "ex": na,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    assert (110 == bit_array_to_int(new_state.get('x').getBits(), na))


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
