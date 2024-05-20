import pytest

from collections import ChainMap
from simulator import *
from XMLExpLexer import XMLExpLexer
from antlr4 import *
from SpecExpParser import *
from SpecExpVisitor import *
from SpecGen import *
from VarCollector import *


####################
## What is input ###

# st : state
# Both inital program and initial values


# env : environment
# How many qubits are in the array


#######################
## What is expected out

# state: dict
# assert that get_state() is equal to the state we expect via oracle


# Write a series of tests HERE
def string_to_program_helper(string: str):
    i_stream = InputStream(string)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    return parser.program()


class TestSimulator(object):
    @pytest.fixture
    def test_result(self, spec: SpecExpParser.ProgramContext, state: dict):
        spec_visitor = SpecGen(state)
        return spec_visitor.visitProgram(spec).getResult()

    @pytest.fixture
    def test_pattern(self, spec: SpecExpParser.ProgramContext):
        var_visitor = VarCollector()
        state = var_visitor.visitProgram(spec)
        # need to use random testing generator to generate values in state
        return self.test_result(spec, state)

    # test_pattern above is rewritten for the usage of pytest.
    # pytest will call test_pattern to test a spec
    # it can also call test_result by inputing a state, and then get
    # the resulting state and check
    # the result state is a list of nat numbers
    # users are responsible to turn the nat numbers to Nvals, then check if
    # the quantum component satisfies with the output
    def test_init(self):
        # We first turn x array to QFT type, and we apply SR gate to rotate the phase of x for 2 pi i * (1/2^10). It will make sense if 10 < rmax, RQFT is the inverse of QFT.
        string = "<pexp gate = 'QFT' > <id> x </id>  <vexp> 0 </vexp> </pexp> <pexp gate = 'SR' > < vexp> 10 </vexp> <id> x </id> </pexp> <pexp gate = 'RQFT' > <id> x </id>  <vexp> 0 </vexp> </pexp> "
        tree = string_to_program_helper(string)
        # print(tree.toStringTree(recog=parser))
        # the following shows an example of using 1 variable state. You can have a 10 variable state
        # see that a variable is a string.
        num_of_qubits = 16
        val = 100  # init value
        val_array = int_to_bool_array(val, num_of_qubits)  # convert value to bool array
        # val = [False]*num # state for x
        state = dict({"x": Coq_nval(val_array, 0)})  # initial a chainMap having variable "x" to be 0 (list of False)
        environment = dict(
            {"x": num_of_qubits})  # env has the same variables as state, but here, variable is initialized to its qubit num
        simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
        simulator.visitProgram(tree)
        new_state = simulator.get_state()
        assert (132 == binary_arr_to_int(new_state.get('x').getBits(), num_of_qubits))

        # Do assertion check that state is as expected
        # int n = binary_arr_to_int(arrayQuBits, sizeArray)
        # assert new_state == state

    def test_qval_sr_1(self):
        string = "<pexp gate = 'SR' > < vexp> 22 </vexp> <id> x </id> </pexp>  <pexp gate = 'RQFT' > <id> x </id>  <vexp> 0 </vexp> </pexp>"
        tree = string_to_program_helper(string)
        num_of_qubits = 8
        val = 11  # init value
        state = dict({"x": Coq_qval(15,20,30)})  # initial a chainMap having variable "x" to be 0 (list of False)
        environment = dict(
            {"x": num_of_qubits})  # env has the same variables as state, but here, variable is initialized to its qubit num
        simulator = Simulator(state, environment)  # Environment is same, initial state varies by pyTest
        simulator.visitProgram(tree)
        new_state = simulator.get_state()
        assert (148 == binary_arr_to_int(simulator.state.get('x').getBits(), num_of_qubits))

    def test_qval_rqft_srr_qft(self):
        string = "<pexp gate='SRR'><vexp>-21</vexp><id>x</id></pexp><pexp gate='RQFT'><id>x</id><vexp>0</vexp></pexp>"
        tree = string_to_program_helper(string)
        num_qubits = 55
        val = 90
        val_array = int_to_bool_array(val, num_qubits)
        state = dict({"x": Coq_qval(16, 20, 30)})
        environment = dict({"x": num_qubits})
        simulator = Simulator(state, environment)
        simulator.visitProgram(tree)
        new_state = simulator.state
        qval = new_state.get("x")
        assert 20 == binary_arr_to_int(qval.bit_array, num_qubits)

    def test_qft_rqft(self):
        string = "<pexp gate='QFT'><id>x</id><vexp>0</vexp></pexp> <pexp gate='RQFT'><id>x</id><vexp>0</vexp></pexp> "
        tree = string_to_program_helper(string)
        num_of_qubits = 11
        val = 120
        val_bit_arr = int_to_bool_array(val, num_of_qubits)
        state = dict({"x": Coq_nval(val_bit_arr, 0)})
        environment = dict({"x": num_of_qubits})
        simulator = Simulator(state, environment)
        simulator.visit(tree)
        assert 120 == binary_arr_to_int(simulator.state.get('x').getBits(), num_of_qubits)

    def test_multiple_sr_and_srr(self):
        string = "<pexp gate='QFT'><id>x</id><vexp>0</vexp></pexp><pexp gate='SR'> <vexp op = '-'>  <id> x </id> <vexp> -10 </vexp> </vexp><id>x</id></pexp><pexp gate='SR'><vexp>-5</vexp><id>x</id></pexp><pexp gate='SR'><vexp>-3</vexp><id>x</id></pexp><pexp gate='SR'><vexp>2</vexp><id>x</id></pexp><pexp gate='SR'><vexp>7</vexp><id>x</id></pexp><pexp gate='SR'><vexp>5</vexp><id>x</id></pexp><pexp gate='RQFT'><id>x</id><vexp>0</vexp></pexp>"
        tree = string_to_program_helper(string)
        num_qubits = 20
        val = 120
        val_bit_arr = int_to_bool_array(val, num_qubits)
        state = dict({"x": Coq_nval(val_bit_arr, 0)})
        environment = dict({"x": num_qubits})
        simulator = Simulator(state, environment)
        simulator.visit(tree)
        assert 120 == binary_arr_to_int(simulator.state.get('x').getBits(), num_qubits)

    def test_reverse_basic(self):
        string = "<pexp gate = 'Rev'> <id> x </id> <vexp> 0 </vexp> </pexp>"
        tree = string_to_program_helper(string)
        num_qubits = 12
        val = 8
        val_array = int_to_bool_array(val, num_qubits)
        state = dict({"x": Coq_nval(val_array, 0)})
        environment = dict(
            {"x": num_qubits})
        simulator = Simulator(state, environment)
        simulator.visitProgram(tree)
        new_state = simulator.get_state()
        assert 256 == binary_arr_to_int(new_state.get('x').getBits(), num_qubits)

    def test_l_shift_basic(self):
        string = "<pexp gate = 'Lshift'> <id> x </id> <vexp> 0 </vexp> </pexp>"
        tree = string_to_program_helper(string)
        num_qubits = 12
        val = 8
        val_array = int_to_bool_array(val, num_qubits)
        state = dict({"x": Coq_nval(val_array, 0)})
        environment = dict(
            {"x": num_qubits})
        simulator = Simulator(state, environment)
        simulator.visitProgram(tree)
        new_state = simulator.get_state()
        assert 16 == binary_arr_to_int(new_state.get('x').getBits(), num_qubits)

    def test_r_shift_basic(self):
        string = "<pexp gate = 'Rshift'> <id> x </id> <vexp> 0 </vexp> </pexp>"
        tree = string_to_program_helper(string)
        num_qubits = 12
        val = 8
        val_array = int_to_bool_array(val, num_qubits)
        state = dict({"x": Coq_nval(val_array, 0)})
        environment = dict(
            {"x": num_qubits})
        simulator = Simulator(state, environment)
        simulator.visitProgram(tree)
        new_state = simulator.get_state()
        assert 4 == binary_arr_to_int(new_state.get('x').getBits(), num_qubits)

    def test_let_basic(self):
        assert True

    def test_match_basic(self):
        assert True

    def test_app_basic(self):
        assert True

    def test_if_basic(self):
        assert True

    def test_skip_basic(self):
        assert True

    def test_x_basic(self):
        assert True

    def test_CU_basic(self):
        assert True

    def test_RZ_basic(self):
        assert True




def test_trivial():
    TestSimulator()
    assert True

if __name__ == "__main__":
    string = ""
    tree = string_to_program_helper(string)
    i_stream = InputStream(string)
    lexer = XMLExpLexer(i_stream)
    t_stream = CommonTokenStream(lexer)
    parser = XMLExpParser(t_stream)
    print(tree.toStringTree(recog=parser))
