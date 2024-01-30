from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from Source.quantumCode.AST_Scripts.ExpParser import ExpParser
from Source.quantumCode.AST_Scripts.ExpVisitor import ExpVisitor

"""
Types
"""


class coq_val:
    pass  # TODO


class Coq_nval(coq_val):

    def __init__(self, b: bool, r: int):
        self.b = b
        self.r = r


class Coq_qval(coq_val):

    def __init__(self, r1: int, r2: int):
        self.r1 = r1
        self.r2 = r2


"""
Helper Functions
"""


def exchange(v: coq_val):
    if isinstance(v, Coq_nval):
        return Coq_nval(not v.b, v.r)
    return v


def get_cua(v):
    if isinstance(v, Coq_nval):
        return v.b
    else:
        return False


def times_rotate(v, q, rmax):
    if isinstance(v, Coq_nval):
        if v.b:
            return Coq_nval(v.b, rotate(v.r, q, rmax))
        else:
            return Coq_nval(v.b, v.r)
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
            return Coq_nval(v.b, r_rotate(v.r, q, rmax))
        else:
            return Coq_nval(v.b, v.r)
    else:
        return Coq_qval(v.r1, r_rotate(v.r2, q, rmax))


def lshift_prime(l, n):
    if n == 0:
        return

    tmp = M_find(0, l)
    for i in range(n - 1):
        M_add(i, M_find(i + 1, l), l)

    M_add(n - 1, tmp, l)

    return l


def rshift_prime(l, n):
    if n == 0:
        return

    tmp = M_find(n - 1, l)
    for i in range(n - 1, -1, -1):
        M_add(i, M_find(i - 1, l), l)

    M_add(0, tmp, l)

    return l


def reverse_prime(l, n):
    if n == 0:
        return
    size = n
    tmp = ChainMap(l)
    for i in range(n):
        M_add(i, M_find(size - i, tmp), l)
    return l

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


# TODO
def assign_r(f, x, r, n, size, rmax):
    pass


# TODO
def a_nat2fb_prime(f, n, acc):
    pass


def a_nat2fb(f, n):
    return a_nat2fb_prime(f, n, 0)


# TODO
def fbrev(n, param):
    pass


# TODO
def get_cus(n, f, x):
    pass


def get_nor_state(x, v, f):
    m = M_find(x, f)
    if isinstance(m, NoneType):
        return Coq_nval(False, 0)
    else:
        return M_find(v, m)


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


"""
Simulator class
  This class extends ExpVisitor, and is essentially an interpreter
  for the OCAML code that we will be testing.
  Follows visitor pattern.
"""


class Simulator(ExpVisitor):

    def __init__(self, st: ChainMap, env: ChainMap):
        self.st = st
        self.env = env
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

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

    # define posi to be a pair of string,int
    def visitPosiexp(self, ctx: ExpParser.PosiexpContext):
        name = ctx.vexp(0).accept(self)
        num = int(ctx.vexp(1).accept(self))
        return name, num

    # should do nothing
    def visitSkipexp(self, ctx: ExpParser.SkipexpContext):
        return

    # X posi, changed the following for an example
    def visitXgexp(self, ctx: ExpParser.XgexpContext):
        x, p = ctx.posiexp().accept(self)  # this will pass the visitor to the child of ctx
        self.st = M_add(x, M_add(p, exchange(get_nor_state(x, p, self.st)), get_nor_state(x, p, self.st)), self.st)

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: ExpParser.CuexpContext):
        x, p = ctx.posiexp().accept(self)
        if get_cua(get_nor_state(x, p, self.st)):
            ctx.exp().accept(self)
        else:
            return  # do nothing

    # my previous rz parsing is wrong
    # it should be RZ q posi
    def visitRzexp(self, ctx: ExpParser.RzexpContext):
        q = int(ctx.vexp().accept(self))  # I guess then you need to define vexp
        # we can first define the var and integer case
        # I guess Identifier and int are all terminal
        # does it means that we do not need to define anything?
        x, p = ctx.posiexp().accept(self)
        st = M_add(x, M_add(p, times_rotate(get_nor_state(x, p, self.st), q, M_find(x, self.env)),
                            get_nor_state(x, p, self.st)), self.st)

    def visitRrzexp(self, ctx: ExpParser.RrzexpContext):
        q = int(ctx.vexp().accept(self))
        x, p = ctx.posiexp().accept(self)
        # p = out[1]
        st = M_add(x, M_add(p, times_r_rotate(get_nor_state(x, p, self.st), q, M_find(x, self.env)),
                            get_nor_state(x, p, self.st)), self.st)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: ExpParser.SrexpContext):
        n = int(ctx.vexp(0).accept(self))
        x = ctx.vexp(1).accept(self)
        self.sr_rotate(x, n)

    def visitSrrexp(self, ctx: ExpParser.SrrexpContext):
        n = int(ctx.vexp(0).accept(self))
        x = ctx.vexp(1).accept(self)
        self.srr_rotate(x, n)

    def lshift(self, x, n):
        return M_add(x, lshift_prime(M_find(x, self.st), n), self.st)

    def visitLshiftexp(self, ctx: ExpParser.LshiftexpContext):
        x = ctx.vexp().accept(self)
        return self.lshift(x, M_find(x, self.env))

    def rshift(self, x, n):
        return M_add(x, rshift_prime(M_find(x, self.st), n), self.st)

    def visitRshiftexp(self, ctx: ExpParser.RshiftexpContext):
        x = ctx.vexp().accept(self)
        return self.rshift(x, M_find(x, self.env))

    def reverse(self, x, n):
        return M_add(x, reverse_prime(M_find(x, self.st), n), self.st)

    def visitRevexp(self, ctx: ExpParser.RevexpContext):
        x = ctx.vexp().accept(self)
        return self.reverse(x, M_find(x, self.env))

    def turn_qft(self, x, n):
        val = M_find(x, self.st)
        r1 = 0
        r2 = 0
        for i in range(n):
            l = M_find(i, val)
            if isinstance(l, Coq_nval):
                r1 += pow(2, i) * l.b % M_find(x, self.env)
                r2 += l.r % M_find(x, self.env)
        M_add(x, Coq_qval(r1, r2), self.st)

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: ExpParser.QftexpContext):
        x = ctx.vexp(0).accept(self)
        b = int(ctx.vexp(1).accept(self))
        self.turn_qft(x, M_find(x, self.env) - b)

    # TODO implement
    def turn_rqft(self, x, n):
        val = M_find(x, self.st)
        if isinstance(val, Coq_qval):
            tmp = val.r1
            tov = ChainMap()
            for i in range(n):
                b = tmp % 2
                tmp = tmp / 2
                M_add(n - i - 1, Coq_nval(b, 0), tov)
            M_add(0, Coq_nval(M_find(0, tov).b, val.r2), tov)
            M_add(x, tov, self.st)

    def visitRqftexp(self, ctx: ExpParser.RqftexpContext):
        x = ctx.vexp(0).accept(self)
        b = int(ctx.vexp(1).accept(self))
        self.turn_rqft(x, M_find(x, self.env) - b)

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    # I doubt you need to define the following from the XMLVisitor example
    # def visitChildren(self, ctx: ParserRuleContext):
    #     out = []
    #     for child in ctx.children:
    #         out.append(self.visit(child))
    #     return out

    # the only thing that matters will be 48 and 47
    def visitTerminal(self, node):
        if node.getSymbol().type == ExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == ExpParser.Number:
            return node.getText()
        return "None"
