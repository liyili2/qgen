from collections import ChainMap
# from types import NoneType

from antlr4 import ParserRuleContext

from XMLExpParser import *
from XMLExpVisitor import *

NoneType = type(None)


class coq_val:
    pass  # TODO


class Coq_nval(coq_val):

    def __init__(self, b: [bool], r: int):
        self.bit_array = b
        self.phase = r

    def getBits(self):
        return self.bit_array

    def getPhase(self):
        return self.phase


class Coq_qval(coq_val):
    """
    A class to represent qval

    Attributes:
        phase (int): phase
        local (int): local
        num (int): num
    """
    def __init__(self, phase: int, local: int, num: int):
        self.phase = phase
        self.local = local
        self.num = num

    def getPhase(self):
        return self.phase

    def getLocal(self):
        return self.local

    def getNum(self):
        return self.num


"""
Helper Functions
"""


def exchange(v: coq_val, n: int):
    if isinstance(v, Coq_nval):
        v.getBits()[n] = not v.getBits()[n]


def times_rotate(v, q, rmax):
    if isinstance(v, Coq_nval):
        if v.bit_array:
            return Coq_nval(v.getBits(), rotate(v.getPhase(), q, rmax))
        else:
            return Coq_nval(v.getBits(), v.getPhase())
    else:
        return Coq_qval(v.phase, rotate(v.local, q, rmax))


def addto(r, n, rmax):
    return (r + 2 ** max_helper(rmax, n)) % 2 ** rmax


def max_helper(x, y):
    return max(x - y, 0)


def rotate(r, n, rmax):
    return addto(r, n, rmax)


def addto_n(r, n, rmax):
    return max_helper(r + 2 ** rmax, 2 ** max_helper(rmax, n)) % 2 ** rmax


def r_rotate(r, n, rmax):
    return addto_n(r, n, rmax)


def times_r_rotate(v, q, rmax):
    if isinstance(v, Coq_nval):
        if v.bit_array:
            return Coq_nval(v.getBits(), r_rotate(v.getPhase(), q, rmax))
        else:
            return Coq_nval(v.getBits(), v.getPhase())
    else:
        return Coq_qval(v.phase, r_rotate(v.local, q, rmax))


def up_h(v, rmax):
    if isinstance(v, Coq_nval):
        b = v.bit_array
        r = v.phase
        if b:
            return Coq_qval(
                r,
                rotate(0, 1, rmax)
            )
        else:
            return Coq_qval(r, 0)
    else:
        r = v.phase
        f = v.local
        return Coq_nval(
            2 ** max_helper(rmax, 1) <= f,
            r
        )


def nat_minus_mod(x, v, a):
    if x - v < 0:
        return x - v + a
    else:
        return x - v


def binary_arr_to_int(array, num_qubits):
    val = 0
    for i in range(num_qubits):
        val += pow(2, i) * int(array[i])
    return val


def int_to_bool_array(v: int, num_qubits: int) -> [bool]:
    val = [False] * num_qubits
    for i in range(num_qubits):
        LSB = v % 2
        v = v // 2
        val[i] = bool(LSB)
    return val


class Simulator(XMLExpVisitor):
    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, state: dict, env: dict):
        self.state = state
        self.env = env
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitLetexp(self, ctx: XMLExpParser.LetexpContext):
        f = ctx.idexp().accept(self)
        self.state.update({f: ctx})
        ctx.exp().accept(self)

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        x = ctx.idexp().accept(self)
        v = self.state.get(x)
        i = 0
        while ctx.exppair(i) is not None:
            if ctx.exppair(i).vexp().OP() is not None:
                va = ctx.exppair(i).vexp().accept(self)
                if v == va:
                    ctx.exppair(i).exp().accept(self)
                    return
            else:
                y = ctx.exppair(i).vexp().idexp().accept(self)
                self.state.update({y: v - 1})
                ctx.exppair(i).exp().accept(self)
            i += 1

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        f = ctx.idexp().accept(self)
        ctxa = self.state.get(f)
        i = 0
        while ctxa.ida(i) is not None:
            x = ctxa.ida(i).Identifier().accept(self)
            v = ctx.vexp(i).accept(self)
            self.state.update({x: v})
            i += 1
        ctxa.exp().accept(self)

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        v = ctx.vexp().accept(self)
        if v == 1:
            ctx.exp(0).accept(self)
        else:
            ctx.exp(1).accept(self)

    def get_state(self):
        return self.state

    def sr_rotate(self, x, vexp_val):
        val = self.state.get(x)
        if isinstance(val, Coq_qval):
            self.state.update(
                {x: Coq_qval(val.phase, (val.local + pow(2, val.num - vexp_val - 1)) % pow(2, val.num), val.num)})

    def srr_rotate(self, x, n):
        val = self.state.get(x)
        if isinstance(val, Coq_qval):
            self.state.update({x: Coq_qval(val.phase, nat_minus_mod(val.local, pow(2, val.getNum() - n - 1),
                                                                    pow(2, val.getNum())), val.getNum())})

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        return

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.idexp().accept(self)
        p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        exchange(self.state.get(x), p)
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.idexp().accept(self)
        p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        if self.state.get(x).getBits()[p]:
            ctx.program().accept(self)
        else:
            return  # do nothing

    # my previous rz parsing is wrong
    # it should be RZ q posi
    def visitRzexp(self, ctx: XMLExpParser.RzexpContext):
        q = int(ctx.vexp(0).accept(self))  # I guess then you need to define vexp
        # we can first define the var and integer case
        # I guess Identifier and int are all terminal
        # does it means that we do not need to define anything?
        x = ctx.idexp().accept(self)
        p = ctx.vexp(1).accept(self)  # this will pass the visitor to the child of ctx
        if q >= 0:
            self.state.update({x: times_rotate(self.state.get(x), q, self.env.get(x))})
        else:
            self.state.update({x: times_r_rotate(self.state.get(x), abs(q), self.env.get(x))})

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        vexp_val = int(ctx.vexp().accept(self))
        x = ctx.idexp().accept(self)
        if vexp_val >= 0:
            self.sr_rotate(x, vexp_val)
        else:
            self.srr_rotate(x, abs(vexp_val))

    def lshift(self, x, n):
        if n == 0:
            return

        tmp = self.state.get(x).getBits()
        tmpv = tmp[0]
        for i in range(n - 1):
            tmp[i] = tmp[i + 1]
        tmp[n - 1] = tmpv
        return self.state.update({x: Coq_nval(tmp, self.state.get(x).getPhase())})

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.idexp().accept(self)
        return self.lshift(x, self.env.get(x))

    def rshift(self, x, n):
        if n == 0:
            return

        tmp = self.state.get(x)
        tmpv = tmp[n - 1]
        for i in range(n - 1, -1, -1):
            tmp[i] = tmp[i - 1]

        tmp[0] = tmpv
        self.state.update({x: Coq_nval(tmp, self.state.get(x).getPhase())})

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.idexp().accept(self)
        return self.rshift(x, self.env.get(x))

    def reverse(self, x, n):
        if n == 0:
            return

        size = n
        tmp = self.state.get(x)
        tmpa = []
        for i in range(n):
            tmpa.append(tmp[size - i])
        self.state.update({x: Coq_nval(tmp, self.state.get(x).getPhase())})

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.idexp().accept(self)
        return self.reverse(x, self.env.get(x))

    def turn_qft(self, x, n):
        selected_state = self.state.get(x)
        phase = selected_state.getPhase()
        local = 0
        if isinstance(selected_state, Coq_nval):
            for i in range(n):
                local = (local + pow(2, i) * int(selected_state.bit_array[i])) % pow(2, n)
        self.state.update({x: Coq_qval(phase, local, n)})

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        ID = ctx.idexp().accept(self)
        vexp = int(ctx.vexp().accept(self))
        self.turn_qft(ID, self.env.get(ID) - vexp)

    # TODO implement
    def turn_rqft(self, x, n):
        selected_state = self.state.get(x)
        if isinstance(selected_state, Coq_qval):
            tmp = selected_state.getLocal()
            tov = [False] * n
            for i in range(n):
                LSB = tmp % 2
                tmp = tmp // 2
                tov[i] = bool(LSB)
            self.state.update({x: Coq_nval(tov, selected_state.phase)})

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.idexp().accept(self)
        vexp_val = int(ctx.vexp().accept(self))
        self.turn_rqft(x, self.env.get(x) - vexp_val)

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        return ctx.Identifier().accept(self)

    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.OP() is None:
            if ctx.numexp() is not None:
                return ctx.numexp().accept(self)
            elif ctx.idexp() is not None:
                x = ctx.idexp().accept(self)
                return self.state.get(x)
            elif ctx.boolexp() is not None:
                if ctx.boolexp().TrueLiteral() is not None:
                    return 1
                else:
                    return 0
        else:
            x = ctx.vexp(0).accept(self)
            y = ctx.vexp(1).accept(self)
            if ctx.OP() == XMLExpParser.Plus:
                return x + y
            elif ctx.OP() == XMLExpParser.Minus:
                return x - y
            elif ctx.OP() == XMLExpParser.Times:
                return x * y
            elif ctx.OP() == XMLExpParser.Div:
                return x // y
            elif ctx.op() == XMLExpParser.GNum:
                return int(x[y])
        return 0

    # the only thing that matters will be 48 and 47
    def visitTerminal(self, node):
        if node.getSymbol().type == XMLExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == XMLExpParser.Number:
            return int(node.getText())
        return "None"
