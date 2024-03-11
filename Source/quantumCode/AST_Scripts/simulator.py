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
        self.b = b
        self.r = r

    def getBits(self):
        return self.b

    def getPhase(self):
        return self.r


class Coq_qval(coq_val):

    def __init__(self, r1: int, r2: int):
        self.r1 = r1
        self.r2 = r2

    def getPhase(self):
        return self.r1

    def getLocal(self):
        return self.r2


"""
Helper Functions
"""


def exchange(v: coq_val, n: int):
    if isinstance(v, Coq_nval):
        v.getBits()[n] = not v.getBits()[n]


def get_cua(v):
    if isinstance(v, Coq_nval):
        return v.b
    else:
        return False


def times_rotate(v, q, rmax):
    if isinstance(v, Coq_nval):
        if v.b:
            return Coq_nval(v.getBits(), rotate(v.getPhase(), q, rmax))
        else:
            return Coq_nval(v.getBits(), v.getPhase())
    else:
        return Coq_qval(v.r1, rotate(v.r2, q, rmax))


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
        if v.b:
            return Coq_nval(v.getBits(), r_rotate(v.getPhase(), q, rmax))
        else:
            return Coq_nval(v.getBits(), v.getPhase())
    else:
        return Coq_qval(v.r1, r_rotate(v.r2, q, rmax))


def up_h(v, rmax):
    if isinstance(v, Coq_nval):
        b = v.b
        r = v.r
        if b:
            return Coq_qval(
                r,
                rotate(0, 1, rmax)
            )
        else:
            return Coq_qval(r, 0)
    else:
        r = v.r1
        f = v.r2
        return Coq_nval(
            2 ** max_helper(rmax, 1) <= f,
            r
        )


def assign_h(f, x, n, i, rmax):
    if n == 0:
        return f
    else:
        m = max(0, n - 1)
        return assign_h(
            M_add(
                {x: n + m},
                up_h(get_state({x: n + m}, f), rmax),
                f
            ),
            x, n, m, rmax
        )


def M_add(k, x, s: ChainMap):
    if len(s.maps) == 0:
        return ChainMap({k: x})
    else:
        p = s.maps[0]
        k_prime, y = next(iter(p.items()))
        if k < k_prime:
            return ChainMap({k: x}, s)
        elif k == k_prime:
            s.__delitem__(k_prime)
            return ChainMap({k: x}, s)
        else:
            s.__delitem__(k_prime)
            return ChainMap({k_prime: y}, M_add(k, x, s))


def M_find(k, M: ChainMap):
    if len(M.maps) == 0:
        return None
    else:
        p = M.maps[0]
        k_prime, x = next(iter(p.items()))
        if k < k_prime:
            return None
        elif k == k_prime:
            return x
        else:
            M.__delitem__(k_prime)
            return M_find(k, M)


def natminusmod(x, v, a):
    if x - v < 0:
        return x - v + a
    else:
        return x - v


def calInt(v, n):
    val = 0
    for i in range(n):
        val += pow(2, i) * int(v[i])
    return val

def calBin(v, n):
    val = [False]*n
    for i in range(n):
        b = v % 2
        v = v // 2
        val[i] = bool(b)
    return val

class Simulator(XMLExpVisitor):
    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, st: ChainMap, env: ChainMap):
        self.st = st
        self.env = env
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def get_state(self):
        return self.st

    def sr_rotate(self, x, n):
        val = M_find(x, self.st)
        if isinstance(val, Coq_qval):
            M_add(x,
                  Coq_qval(val.r1, (val.r2 + pow(2, M_find(x, self.env) - n - 1)) % pow(2, M_find(x, self.env))),
                  self.st)

    def srr_rotate(self, x, n):
        val = M_find(x, self.st)
        if isinstance(val, Coq_qval):
            M_add(x,
                  Coq_qval(val.r1, natminusmod(val.r2, pow(2, M_find(x, self.env) - n - 1), M_find(x, self.env))),
                  self.st)

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        return

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.idexp().accept(self)
        p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        print("herea")
        print(x)
        print("ad:")
        print(p)
        exchange(M_find(x, self.st), p)
        #print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.idexp().accept(self)
        p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        if get_cua(M_find(x, self.st)(x, self.st).getBits()[p]):
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
            M_add(x, times_rotate(M_find(x, self.st), p, M_find(x, self.env)), self.st)
            get_nor_state(x, p, self.st)[p] = times_rotate(get_nor_state(x, p, self.st), q, M_find(x, self.env))
        else:
            M_add(x, times_r_rotate(M_find(x, self.st), p, M_find(x, self.env)), self.st)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        n = int(ctx.vexp().accept(self))
        x = ctx.idexp().accept(self)
        if n >= 0:
            self.sr_rotate(x, n)
        else:
            self.srr_rotate(x, abs(n))

    def lshift(self, x, n):
        if n == 0:
            return

        tmp = M_find(x, self.st).getBits()
        tmpv = tmp[0]
        for i in range(n - 1):
            tmp[i] = tmp[i + 1]
        tmp[n - 1] = tmpv
        return M_add(x, Coq_nval(tmp, M_find(x, self.st).getPhase()), self_st)

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.idexp().accept(self)
        return self.lshift(x, M_find(x, self.env))

    def rshift(self, x, n):
        if n == 0:
            return

        tmp = M_find(x, self.st)
        tmpv = tmp[n - 1]
        for i in range(n - 1, -1, -1):
            tmp[i] = tmp[i - 1]

        tmp[0] = tmpv
        M_add(x, Coq_nval(tmp, M_find(x, self.st).getPhase()), self.st)

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.idexp().accept(self)
        return self.rshift(x, M_find(x, self.env))

    def reverse(self, x, n):
        if n == 0:
            return

        size = n
        tmp = M_find(x, self.st)
        tmpa = []
        for i in range(n):
            tmpa.append(tmp[size - i])
        M_add(x, Coq_nval(tmp, M_find(x, self.st).getPhase()), self.st)

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.idexp().accept(self)
        return self.reverse(x, M_find(x, self.env))

    def turn_qft(self, x, n):
        val = M_find(x, self.st)
        r1 = val.getPhase()
        r2 = 0
        for i in range(n):
            l = val[i]
            if isinstance(l, Coq_nval):
                r2 += pow(2, i) * int(l.getBits()[i]) % M_find(x, self.env)
        M_add(x, Coq_qval(r1, r2), self.st)

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.idexp().accept(self)
        b = int(ctx.vexp().accept(self))
        self.turn_qft(x, M_find(x, self.env) - b)

    # TODO implement
    def turn_rqft(self, x, n):
        val = M_find(x, self.st)
        if isinstance(val, Coq_qval):
            tmp = val.getLocal()
            tov = [False] * n
            for i in range(n):
                b = tmp % 2
                tmp = tmp / 2
                tov[n - i - 1] = bool(b)
            M_add(x, Coq_nval(tov, val.r2), self.st)

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.idexp().accept(self)
        b = int(ctx.vexp().accept(self))
        self.turn_rqft(x, M_find(x, self.env) - b)

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    def visitIdexp(self, ctx:XMLExpParser.IdexpContext):
        return ctx.Identifier().accept(self)

    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx:XMLExpParser.VexpContext):
        return ctx.numexp().accept(self)

    # the only thing that matters will be 48 and 47
    def visitTerminal(self, node):
        if node.getSymbol().type == XMLExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == XMLExpParser.Number:
            return int(node.getText())
        return "None"
