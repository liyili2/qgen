import time
import pytest
from antlr4 import InputStream, CommonTokenStream
from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import CoqNVal, Simulator, bit_array_to_int, to_binary_arr


# Test function to initialize and run the rz_adder simulation
def run_rz_adder_test(num_qubits, loop, val,addend):
    with open("Benchmark/rz_adder/rz_adder_good.xml", 'r') as f:
        str = f.read()
    i_stream = InputStream(str)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    tree = parser.root()
    # print(tree.toStringTree(recog=parser))

    # num_qubits = 16  # Number of Qubits
    # val = 100  # init value
    # addend = 10
    val_array = to_binary_arr(val, num_qubits)  # conver value to array
    state = dict({"x": [CoqNVal(val_array, 0)],
                  "na": loop,
                  "size": num_qubits,
                  "m": addend})  # initial a chainMap having variable "x" to be 0 (list of False)
    environment = dict(
        {"x": num_qubits})  # env has the same variables as state, but here, variable is initiliazed to its qubit num
    y = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
    y.visitRoot(tree)
    new_state = y.get_state()
    return bit_array_to_int(new_state.get('x')[0].getBits(), num_qubits)

'''
This test verifies the correctness of the rz_adder function when performing
simple addition operations without carry propagation.
    ''' 
@pytest.mark.parametrize("num_qubits, loop, val, addend", [
    (2**n, loop, val, addend)
    for n in range(2, 4)  # Using 2^2, 2^3, i.e., 4, 8
    for loop in range(1, 2**n)
    for val in range(0, 2**(2**n),2*7)  # Range for val up to 2^num_qubits
    for addend in range(0, 2**(2**n),2*19)  # interval as product of primes
])

def test_basic_addition(num_qubits, loop, val, addend):
    expected = (val + addend) % (2 ** loop) #might not be correct
    assert run_rz_adder_test(num_qubits, loop, val, addend) == expected

'''
  In this test, we check whether the rz_adder correctly handles carry propagation by adding values close to the upper limit 
  of the bit range and ensuring that the result wraps around correctly.
'''

@pytest.mark.parametrize("num_qubits, loop, val, addend", [
    (2**n, loop, val, addend)
    for n in range(2, 4)  # This gives us 2^2 = 4 and 2^3 = 8
    for loop in range(1, 2**n)
    for val in range(2**(2**n)//2, 2**(2**n), 2*7)  #interval as product of primes
    for addend in range(1, 2**(2**n), 2*19) 
][:40])  # Limiting to first 40 combinations

def test_carry_propagation(num_qubits, loop, val, addend):
    expected = (val + addend) % (2 ** loop)  #might not be correct
    assert run_rz_adder_test(num_qubits, loop, val, addend) == expected

'''Testing array sizelimit
   It ensures that the rz_adder correctly wraps around the result within the allowed
   bit range (num_qubits).
'''
@pytest.mark.parametrize("num_qubits, loop, val, addend", [
    (2**n, loop, val, addend)
    for n in range(2, 4)
    for loop in range(1, 2**n)
    for val in range(0, 2**(2**n)//2,2*7)  # Testing small values
    for addend in range(2**(2**n)//2, 2**(2**n),2*19)  # Adding large values
])

def test_array_size_limit(num_qubits, loop, val, addend):
    expected = (val + addend) % (2 ** loop)
    assert run_rz_adder_test(num_qubits, loop, val, addend) == expected

#Testing large numbers

@pytest.mark.parametrize("num_qubits, loop, val, addend", [
    (2**n, 2**n, 2**32, 2**32)
    for n in range(4, 5)
    for loop in range(1, 2**n)
])

def test_large_numbers(num_qubits, loop, val, addend):
    expected = (val + addend) % (2 ** loop)
    assert run_rz_adder_test(num_qubits, loop, val, addend) == expected

#Testing addend as 0

@pytest.mark.parametrize("num_qubits, loop, val, addend", [
    (2**n, loop, val, 0)
    for n in range(4, 5)  # Using 2^4 = 16
    for loop in range(1, 2**n)
    for val in range(0, 40, 5)
])


def test_zero_addend(num_qubits, loop, val, addend):
    expected = val
    assert run_rz_adder_test(num_qubits, loop, val, addend) == expected

#Testing qubit_array as 0

@pytest.mark.parametrize("num_qubits, loop, val, addend", [
    (2**n, loop, 0, addend)
    for n in range(4, 5)  # Using 2^4 = 16
    for loop in range(1, 2**n)
    for addend in range(0, 40, 5)
])

def test_zero_qubit_array(num_qubits, loop, val, addend):
    expected = addend
    assert run_rz_adder_test(num_qubits, loop, val, addend) == expected


@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)

