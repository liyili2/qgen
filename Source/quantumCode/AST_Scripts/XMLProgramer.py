from types import NoneType


class QXTop:
    pass


class QXRoot(QXTop):
    def __init__(self, program: QXProgram):
        self.program = program


class QXNext(QXTop):
    def __init__(self, program: QXProgram):
        self.program = program


class QXProgram(QXTop):
    def __init__(self, exps: [QXExp]):
        self.exps = exps


class QXExp(QXTop):
    pass


class QXLet(QXExp):
    def __init__(self, id: string, ids: [QXIdExp], p: QXProgram):
        self.id = id
        self.ids = ids
        self.prog = p


class QXApp(QXExp):
    def __init__(self, id: string, vs: [QXVexp]):
        self.id = id
        self.vs = vs


class QXBlock(QXExp):
    pass


class QXCU(QXExp):
    def __init__(self, id: string, v: QXVexp, p: QXProgram):
        self.id = id
        self.v = v
        self.prog = p


class QXIf(QXExp):
    def __init__(self, v: QXVexp, left: QXNext, right: QXNext):
        self.v = v
        self.left = left
        self.right = right


class QXMatch(QXExp):
    def __init__(self, v: string, zero: QXPair, multi: QXPair):
        self.id = v
        self.zero = zero
        self.multi = multi


class QXPair(QXTop):
    def __init__(self, v: QXElem, p: QXProgram):
        self.v = v
        self.prog = p


class QXElem(QXTop):
    pass


class QXVexp(QXTop):
    pass


class QXBin(QxVexp):
    def __init__(self, op: string, v1: QxVexp, v2: QxVexp):
        self.op = op
        self.v1 = v1
        self.v2 = v2


class QXNum(QXElem, QXVexp):
    def __init__(self, v: int):
        self.v = v


class QXIDExp(QXElem, QXVexp):
    def __init__(self, v: string, type: QXType = None):
        self.v = v
        self.type = type


class QXType(QXTop):
    pass


class Qty(QXType):

    def __init__(self, qubit_array_size, type: str = None, m=None):
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


class Nat(QXType):

    def type(self):
        return "Nat"


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


class QXSKIP(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v


class QXX(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v


class QXSR(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v


class QXQFT(QXExp):
    def __init__(self, id: string, v: QXVexp):
        self.id = id
        self.v = v


class QXRQFT(QXExp):
    def __init__(self, id: string):
        self.id = id


class QXLshift(QXExp):
    def __init__(self, id: string):
        self.id = id


class QXRshift(QXExp):
    def __init__(self, id: string):
        self.id = id


class QXRev(QXExp):
    def __init__(self, id: string):
        self.id = id
