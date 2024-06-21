import time
import pytest
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import CoqNVal, Simulator, bit_array_to_int, to_binary_arr


# Test function to initialize and run the rz_adder simulation
def run_rz_adder_test(num_qubits,val,addend):
    with open("Benchmark/rz_adder/rz_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.root()
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


@pytest.mark.parametrize("num_qubits, val, addend", [
    (2**n, val, addend)
    for n in range(2, 4)  # Using 2^2, 2^3, 2^4, i.e., 4, 8, 16
    for val in range(0, 2**(2**n),20)  # Range for val up to 2^num_qubits
    for addend in range(0, 2**(2**n),100)  # Range for addend up to 2^num_qubits
])

def test_basic_addition(num_qubits, val, addend):
    expected = (val + addend) % (2 ** num_qubits)
    assert run_rz_adder_test(num_qubits, val, addend) == expected


@pytest.mark.parametrize("num_qubits, val, addend", [
    (2**n, val, addend)
    for n in range(2, 4)  # This gives us 2^2 = 4 and 2^3 = 8
    for val in range(2**(2**n)//2, 2**(2**n), 2**n)  # Adjusted step size for fewer values
    for addend in range(1, 2**(2**n), 2**n)  # Adjusted step size for fewer values
][:40])  # Limiting to first 40 combinations

def test_carry_propagation(num_qubits, val, addend):
    expected = (val + addend) % (2 ** num_qubits)
    assert run_rz_adder_test(num_qubits, val, addend) == expected

@pytest.mark.parametrize("num_qubits, val, addend", [
    (2**n, val, addend)
    for n in range(2, 4)
    for val in range(0, 2**(2**n)//2,30)  # Testing small values
    for addend in range(2**(2**n)//2, 2**(2**n),30)  # Adding large values
])
def test_array_size_limit(num_qubits, val, addend):
    expected = (val + addend) % (2 ** num_qubits)
    assert run_rz_adder_test(num_qubits, val, addend) == expected

@pytest.mark.parametrize("num_qubits, val, addend", [
    (2**n, 2**32, 2**32)
    for n in range(4, 5)  
])
def test_large_numbers(num_qubits, val, addend):
    expected = (val + addend) % (2 ** num_qubits)
    assert run_rz_adder_test(num_qubits, val, addend) == expected

@pytest.mark.parametrize("num_qubits, val, addend", [
    (2**n, val, 0)
    for n in range(4, 5)  # Using 2^4 = 16
    for val in range(0, 40, 5)
])
def test_zero_addend(num_qubits, val, addend):
    expected = val
    assert run_rz_adder_test(num_qubits, val, addend) == expected

@pytest.mark.parametrize("num_qubits, val, addend", [
    (2**n, 0, addend)
    for n in range(4, 5)  # Using 2^4 = 16
    for addend in range(0, 40, 5)
])
def test_zero_qubit_array(num_qubits, val, addend):
    expected = addend
    assert run_rz_adder_test(num_qubits, val, addend) == expected


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)

