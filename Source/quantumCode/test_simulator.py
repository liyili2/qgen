import pytest

from simulator import *

####################
## What is input ###

# st : state
# Both inital program and initial values


# env : environment
# How many qubits are in the array


#######################
## What is expected out

# st : state
# assert that get_state() is equal to the state we expect via oracle


# Write a series of tests HERE
class Test_Simulator(object):

    def test_init(self):
        # //We first turn x array to QFT type, and we apply SR gate to rotate the phase of x for 2 pi i * (1/2^10). It will make sense if 10 < rmax, RQFT is the inverse of QFT.
        str = "QFT x 0; SR 10 x; RQFT x 0 "
        i_stream = InputStream(str)
        lexer = ExpLexer(i_stream)
        t_stream = CommonTokenStream(lexer)
        parser = ExpParser(t_stream)
        tree = parser.program()
        print(tree.toStringTree(recog=parser))

        state = True
        environment = 10 # Number of Qubits
        y = Simulator(state, environment) # Environment is same, initial state varies by pyTest
        y.visitProgram(tree)
        newState = y.get_state()

        # Do assertion check that state is as expected
        # Add function to do state (binary-> int ) conversion  #TODO#
        # int n = calInt(arrayQuBits, sizeArray)
        assert newState == state