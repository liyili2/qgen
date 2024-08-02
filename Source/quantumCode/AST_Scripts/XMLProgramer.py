from types import NoneType
from Source.quantumCode.AST_Scripts.ProgramVisitor import *

class QXTop:

    def accept(self, visitor):
        pass


class QXRoot(QXTop):
    def __init__(self, program: QXProgram):
        self.program = program

    def accept(self, visitor : ProgramVisitor):
        visitor.visitRoot(self)

    def program(self):
        return self.program


class QXNext(QXTop):
    def __init__(self, program: QXProgram):
        self.program = program

    def accept(self, visitor : ProgramVisitor):
        visitor.visitNext(self)

    def program(self):
        return self.program


class QXProgram(QXTop):
    def __init__(self, exps: [QXExp]):
        self.exps = exps

    def accept(self, visitor : ProgramVisitor):
        visitor.visitProgram(self)

    def exp(self, i:int=None):
        return self.exps[i]


class QXExp(QXTop):

    def accept(self, visitor : ProgramVisitor):
        pass


class QXLet(QXExp):
    def __init__(self, id: string, ids: [QXIdExp], p: QXProgram):
        self.id = id
        self.ids = ids
        self.prog = p

    def accept(self, visitor : ProgramVisitor):
        visitor.visitLet(self)

    def ID(self):
        return self.id

    def idexp(self, i:int = None):
        return self.ids[i]

    def program(self):
        return self.prog

class QXApp(QXExp):
    def __init__(self, id: string, vs: [QXVexp]):
        self.id = id
        self.vs = vs

    def accept(self, visitor : ProgramVisitor):
        visitor.visitApp(self)

    def ID(self):
        return self.id

    def vexp(self, i : int = None):
        return self.vs[i]


class QXBlock(QXExp):

    def accept(self, visitor : ProgramVisitor):
        visitor.visitBlock(self)



class QXCU(QXExp):
    def __init__(self, id: string, v: QXVexp, p: QXProgram):
        self.id = id
        self.v = v
        self.prog = p

    def accept(self, visitor : ProgramVisitor):
        visitor.visitCU(self)

    def ID(self):
        return self.id

    def vexp(self):
        return self.v

    def program(self):
        return self.prog


class QXIf(QXExp):
    def __init__(self, v: QXVexp, left: QXNext, right: QXNext):
        self.v = v
        self.left = left
        self.right = right

    def accept(self, visitor : ProgramVisitor):
        visitor.visitIf(self)

    def vexp(self):
        return self.v

    def left(self):
        return self.left

    def right(self):
        return self.right


class QXMatch(QXExp):
    def __init__(self, v: string, zero: QXPair, multi: QXPair):
        self.id = v
        self.zero = zero
        self.multi = multi

    def accept(self, visitor : ProgramVisitor):
        visitor.visitMatch(self)

    def ID(self):
        return self.v

    def zero(self):
        return self.zero

    def multi(self):
        return self.multi


class QXPair(QXTop):
    def __init__(self, v: QXElem, p: QXProgram):
        self.v = v
        self.prog = p

    def accept(self, visitor : ProgramVisitor):
        visitor.visitPair(self)

    def elem(self):
        return self.v

    def program(self):
        return self.prog


class QXElem(QXTop):

    def accept(self, visitor : ProgramVisitor):
        pass


class QXVexp(QXTop):

    def accept(self, visitor : ProgramVisitor):
        pass


class QXBin(QxVexp):
    def __init__(self, op: string, v1: QxVexp, v2: QxVexp):
        self.op = op
        self.v1 = v1
        self.v2 = v2

    def accept(self, visitor : ProgramVisitor):
        visitor.visitBin(self)


    def OP(self):
        return self.op

    def left(self):
        return self.v1

    def right(self):
        return self.v2


class QXNum(QXElem, QXVexp):
    def __init__(self, v: int):
        self.v = v

    def accept(self, visitor : ProgramVisitor):
        visitor.visitNum(self)

    def num(self):
        return self.v


class QXIDExp(QXElem, QXVexp):
    def __init__(self, v: string, type: QXType = None):
        self.v = v
        self.type = type

    def accept(self, visitor : ProgramVisitor):
        visitor.visitIDExp(self)

    def ID(self):
        return self.v

    def type(self):
        return self.type

def joinType(a: TypeName, b: TypeName):
    if isinstance(a, Qty) and isinstance(b, Qty):
        if a.type() is None or b.type() is None:
            if a.type() is None:
                a.set_type(b.type())
            else:
                b.set_type(a.type())
            return a
        elif a.type() == b.type():
            return a
        else:
            return None
    elif isinstance(a, Nat) and isinstance(b, Nat):
        return a
    elif isinstance(a, Fun) and isinstance(b, Fun):
        return a
    else:
        return None


def joinTypes(a: dict, b: dict):
    for key in a.keys():
        if b.get(key) is not None:
            if isinstance(a.get(key), Qty) and isinstance(b.get(key), Qty):
                if a.get(key).type() is None and b.get(key).type() is not None:
                    a.get(key).set_type(b.get(key).type())
    return a


def equalTypes(a: dict, b: dict):
    tmp = True
    for key in a.keys():
        if a.get(key) != b.get(key):
            tmp = False
    return tmp

class QXType(QXTop):

    def accept(self, visitor : ProgramVisitor):
        pass


class Qty(QXType):

    def __init__(self, qubit_array_size: QXElem, type: str = None, m=None):
        self.qubit_array_size = qubit_array_size
        self.type = type
        if m is None:
            self.m = "0"
        else:
            self.m = m

    def get_num(self):
        return self.qubit_array_size

    def get_anum(self):
        return self.m

    def set_type(self, ty: str):
        self.type = ty

    def type(self):
        return self.type

    def fullty(self):
        return (self.type, self.qubit_array_size, self.m)

    def __str__(self):
        return f"Qty(type={self.type}, qubit_array_size={self.qubit_array_size}, m={self.m})"

    def accept(self, visitor : ProgramVisitor):
        visitor.visitQty(self)

class Nat(QXType):

    def type(self):
        return "Nat"

    def accept(self, visitor : ProgramVisitor):
        visitor.visitNat(self)

class Fun(QXType):

    def __init__(self, args: [str], pre: dict, out: dict):
        self.args = args
        self.pre = pre
        self.out = out
        # self.r2 = r2

    def type(self):
        return ("Fun", (self.args, self.pre, self.out))

    def args(self):
        return self.args

    def pre(self):
        return self.pre

    def out(self):
        return self.out

    def __str__(self):
        return f"Fun(args={self.args}, pre={self.pre}, out={self.out})"

    def accept(self, visitor : ProgramVisitor):
        visitor.visitFun(self)


class QXSKIP(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v

    def accept(self, visitor : ProgramVisitor):
        visitor.visitSKIP(self)

    def ID(self):
        return self.id

    def vexp(self):
        return self.v


class QXX(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v

    def accept(self, visitor : ProgramVisitor):
        visitor.visitX(self)

    def ID(self):
        return self.id

    def vexp(self):
        return self.v


class QXSR(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v

    def accept(self, visitor : ProgramVisitor):
        visitor.visitSR(self)

    def ID(self):
        return self.id

    def vexp(self):
        return self.v


class QXQFT(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v

    def accept(self, visitor : ProgramVisitor):
        visitor.visitQFT(self)

    def ID(self):
        return self.id

    def vexp(self):
        return self.v


class QXRQFT(QXExp):
    def __init__(self, id: string):
        self.id = id

    def accept(self, visitor : ProgramVisitor):
        visitor.visitRQFT(self)

    def ID(self):
        return self.id


class QXLshift(QXExp):
    def __init__(self, id: string):
        self.id = id

    def accept(self, visitor : ProgramVisitor):
        visitor.visitLshift(self)

    def ID(self):
        return self.id

class QXRshift(QXExp):
    def __init__(self, id: string):
        self.id = id

    def accept(self, visitor : ProgramVisitor):
        visitor.visitRshift(self)

    def ID(self):
        return self.id


class QXRev(QXExp):
    def __init__(self, id: string):
        self.id = id

    def accept(self, visitor : ProgramVisitor):
        visitor.visitRev(self)

    def ID(self):
        return self.id
