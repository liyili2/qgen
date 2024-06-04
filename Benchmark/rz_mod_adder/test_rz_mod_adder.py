import time
import pytest
from antlr4 import InputStream, CommonTokenStream

from Source.quantumCode.AST_Scripts.XMLExpLexer import XMLExpLexer
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.simulator import to_binary_arr, CoqNVal, Simulator, bit_array_to_int


def test_full_rz_mod_adder():
    with open("Benchmark/rz_mod_adder/rz_mod_adder_good.xml", 'r') as f:
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

    val_carry_reg = 0
    num_qubits_carry = 1
    val_array_carry = to_binary_arr(val_carry_reg, num_qubits_carry)

    addend = 5

    modulo = 16

    state = dict(
        {"x": CoqNVal(val_array_x, 0),
         "c": CoqNVal(val_array_carry, 0),
         "na": na,
         "a": addend,
         "m": modulo,
         })
    environment = dict(
        {"x": num_qubits_x,
         "c": num_qubits_carry,
         })
    simulator = Simulator(state, environment)
    simulator.visitProgram(tree)
    new_state = simulator.get_state()
    assert (110 == bit_array_to_int(new_state.get('x').getBits(), num_qubits_x))

        
@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
