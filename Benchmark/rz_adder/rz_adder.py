import time
import pytest
from triangle import TriangleType, classify_triangle # this might not be correct


def check_classification(triangles, expected_result):
    for triangle in triangles:
        assert classify_triangle(*triangle) == expected_result


def test_invalid_triangles():
    triangles = [(1, 2, 9), (1, 9, 2), (2, 1, 9), (2, 9, 1), (9, 1, 2),
                 (9, 2, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
    check_classification(triangles, TriangleType.INVALID)


def test_equalateral_triangles():
    triangles = [(1, 1, 1), (100, 100, 100), (99, 99, 99)]
    check_classification(triangles, TriangleType.EQUALATERAL)


def test_isoceles_triangles():
    triangles = [(100, 90, 90), (90, 100, 90), (90, 90, 100), (3, 3, 2), (3, 2, 3), (2, 3, 3)]

    check_classification(triangles, TriangleType.ISOCELES)


def test_scalene_triangles():
    triangles = [(5, 4, 3), (5, 3, 4), (4, 5, 3), (4, 3, 5), (3, 5, 4)]
    check_classification(triangles, TriangleType.SCALENE)


def test_init(self):
        # //We first turn x array to QFT type, and we apply SR gate to rotate the phase of x for 2 pi i * (1/2^10). It will make sense if 10 < rmax, RQFT is the inverse of QFT.
        str = ... # load string from rz_adder.xml
        i_stream = InputStream(str)
        lexer = XMLExpLexer(i_stream)
        t_stream = CommonTokenStream(lexer)
        parser = XMLExpParser(t_stream)
        tree = parser.program()
        print(tree.toStringTree(recog=parser))

        # the following shows an example of using 1 variable state. You can have a 10 variable state
        # see that a variable is a string.
        num = 16 # Number of Qubits
        val = 100 #init value
        valArray = calBin(val,num) #conver value to array
        #val = [False]*num # state for x
        state = dict({"x" : Coq_nval(valArray,0), "M" : val}) #initial a chainMap having variable "x" to be 0 (list of False)
        environment = dict({"x" : num}) #env has the same variables as state, but here, variable is initiliazed to its qubit num
        y = Simulator(state, environment) # Environment is same, initial state varies by pyTest
        y.visitProgram(tree)
        newState = y.get_state()
        assert(132 == calInt(newState.get('x').getBits(), num))

        # Do assertion check that state is as expected
        # Add function to do state (binary-> int ) conversion  #TODO#
        # int n = calInt(arrayQuBits, sizeArray)
        #assert newState == state
        
        
@pytest.fixture(scope="session", autouse=True)
def starter(request):
    start_time = time.time()

    def finalizer():
        print("runtime: {}".format(str(time.time() - start_time)))

    request.addfinalizer(finalizer)
