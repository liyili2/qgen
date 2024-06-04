import time
import pytest
from antlr4 import InputStream, CommonTokenStream

# from Benchmark.Triangle.triangle import TriangleType, classify_triangle # this might not be correct
from Benchmark.cl_adder.cl_adder_const import X_CCV, FLIP_X_ZERO_ROTATE_PHASE, CNOT, CCX
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import to_binary_arr, CoqNVal, Simulator, bit_array_to_int

# for the first step, the fitness is the percentage of correctness. How many test cases a program run correctly.
# the correctness is defined as array, x, y and c, the input is (x,y,c), and the output is (x,x+y,c)

def test_skip():
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
    num_qubits_x = 16  # Number of Qubits
    val_x = 100  # init value
    val_array_x = to_binary_arr(val_x, num_qubits_x)  # convert value to array
    num_qubits_y = 64
    val_y = 10
    val_array_y = to_binary_arr(val_y, num_qubits_y)
    val_ca = 20
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)
    na = 7
    state = dict(
        {"xa": CoqNVal(val_array_x, 0),
         "ya": CoqNVal(val_array_y, 0),
         "ca": CoqNVal(val_array_ca, 0),
         "na": na,
         })
    environment = dict(
        {"xa": num_qubits_x,
         "ya": num_qubits_y,
         "ca": num_qubits_ca,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    assert (11 == bit_array_to_int(new_state.get('ya').getBits(), num_qubits_y))

def test_x_ccv():
    str = X_CCV
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    num_qubits_x = 16  # Number of Qubits
    val_x = 100  # init value
    val_array_x = to_binary_arr(val_x, num_qubits_x)  # convert value to array
    num_qubits_y = 64
    val_y = 10
    val_array_y = to_binary_arr(val_y, num_qubits_y)
    val_ca = 20
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)
    na = 7
    # val = [False]*num # state for x
    state = dict(
        {"xa": CoqNVal(val_array_x, 0),
         "ya": CoqNVal(val_array_y, 0),
         "ca": CoqNVal(val_array_ca, 0),
         "na": na,
         })
    environment = dict(
        {"xa": num_qubits_x,
         "ya": num_qubits_y,
         "ca": num_qubits_ca,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    # print(calInt(new_state.get('xa').getBits(), num_qubits_x) )
    assert (10 == bit_array_to_int(new_state.get('ya').getBits(), num_qubits_y))

def test_flip_x_rotate_zero():
    str = FLIP_X_ZERO_ROTATE_PHASE
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    num_qubits_x = 16  # Number of Qubits
    val_x = 100  # init value
    val_array_x = to_binary_arr(val_x, num_qubits_x)  # convert value to array
    num_qubits_y = 64
    val_y = 10
    val_array_y = to_binary_arr(val_y, num_qubits_y)
    val_ca = 20
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)
    na = 7
    # val = [False]*num # state for x
    state = dict(
        {"xa": CoqNVal(val_array_x, 0),
         "ya": CoqNVal(val_array_y, 0),
         "ca": CoqNVal(val_array_ca, 0),
         "na": na,
         })
    environment = dict(
        {"xa": num_qubits_x,
         "ya": num_qubits_y,
         "ca": num_qubits_ca,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    # print(calInt(new_state.get('xa').getBits(), num_qubits_x) )
    assert (10 == bit_array_to_int(new_state.get('ya').getBits(), num_qubits_y))

def test_cnot_basic():
    str = CNOT
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    num_qubits_x = 16  # Number of Qubits
    val_x = 100  # init value
    val_array_x = to_binary_arr(val_x, num_qubits_x)  # convert value to array
    num_qubits_y = 64
    val_y = 10
    val_array_y = to_binary_arr(val_y, num_qubits_y)
    val_ca = 20
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)
    na = 7
    # val = [False]*num # state for x
    state = dict(
        {"xa": CoqNVal(val_array_x, 0),
         "ya": CoqNVal(val_array_y, 0),
         "ca": CoqNVal(val_array_ca, 0),
         "na": na,
         })
    environment = dict(
        {"xa": num_qubits_x,
         "ya": num_qubits_y,
         "ca": num_qubits_ca,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    # print(calInt(new_state.get('xa').getBits(), num_qubits_x) )
    assert (10 == bit_array_to_int(new_state.get('ya').getBits(), num_qubits_y))

def test_ccx_basic():
    str = CCX
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    num_qubits_x = 16  # Number of Qubits
    val_x = 100  # init value
    val_array_x = to_binary_arr(val_x, num_qubits_x)  # convert value to array
    num_qubits_y = 64
    val_y = 10
    val_array_y = to_binary_arr(val_y, num_qubits_y)
    val_ca = 20
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)
    na = 7
    # val = [False]*num # state for x
    state = dict(
        {"xa": CoqNVal(val_array_x, 0),
         "ya": CoqNVal(val_array_y, 0),
         "ca": CoqNVal(val_array_ca, 0),
         "na": na,
         })
    environment = dict(
        {"xa": num_qubits_x,
         "ya": num_qubits_y,
         "ca": num_qubits_ca,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    # print(calInt(new_state.get('xa').getBits(), num_qubits_x) )
    assert (10 == bit_array_to_int(new_state.get('ya').getBits(), num_qubits_y))

def test_full_cl_adder():
    with open("Benchmark/cl_adder/cl_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    na = 16

    num_qubits_x = na
    val_x = 10
    val_array_x = to_binary_arr(val_x, num_qubits_x)

    num_qubits_y = na
    val_y = 10
    val_array_y = to_binary_arr(val_y, num_qubits_y)

    val_ca = 0
    num_qubits_ca = 1
    val_array_ca = to_binary_arr(val_ca, num_qubits_ca)


    state = dict(
        {"xa": CoqNVal(val_array_x, 0),
         "ya": CoqNVal(val_array_y, 0),
         "ca": CoqNVal(val_array_ca, 0),
         "na": na,
         })
    environment = dict(
        {"xa": num_qubits_x,
         "ya": num_qubits_y,
         "ca": num_qubits_ca,
         })
    # env has the same variables as state, but here, variable is initiliazed to its qubit num
    simulator = Simulator(state, environment)
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    assert (20 == bit_array_to_int(new_state.get('ya').getBits(), num_qubits_y))







@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
