from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from Source.quantumCode.AST_Scripts.ExpParser import SkipexpContext, CuexpContext, RzexpContext, RrzexpContext, \
    SrexpContext, SrrexpContext, LshiftexpContext, RshiftexpContext, RevexpContext, QftexpContext, RqftexpContext, \
    SeqexpContext
from Source.quantumCode.AST_Scripts.ExpVisitor import ExpVisitor

"""
Types
"""


class coq_val:
    pass


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


def get_state(p, f):
    x = M_find(p, f)
    if isinstance(x, NoneType):
        return Coq_nval(False, 0)
    else:
        return x


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


def sr_rotate_prime(st, x, n, size, rmax):
    if n == 0:
        return st
    else:
        m = max(0, n - 1)
        return sr_rotate_prime(
            M_add(
                {x: m},
                times_rotate(get_state({x: m}, st), max_helper(size, m), rmax),
                st
            ),
            x, m, size, rmax
        )


def sr_rotate(st, x, n, rmax):
    return sr_rotate_prime(st, x, n + 1, n + 1, rmax)


def srr_rotate_prime(st, x, n, size, rmax):
    if n == 0:
        return st
    else:
        m = max(0, n - 1)
        return srr_rotate_prime(
            M_add(
                {x: m},
                times_r_rotate(get_state({x: m}, st), max_helper(size, m), rmax),
                st
            ),
            x, m, size, rmax
        )


def srr_rotate(st, x, n, rmax):
    return srr_rotate_prime(st, x, n + 1, n + 1, rmax)


def lshift_prime(n, size, f, x):
    if n == 0:
        return M_add({x: 0}, get_state({x: size}, f), f)
    else:
        m = max(0, n - 1)
        return M_add({x: n}, get_state({x: m}, f), lshift_prime(m, size, f, x))


def lshift(f, x, n):
    return lshift_prime(max_helper(n, 1), max_helper(n, 1), f, x)


def rshift_prime(n, size, f, x):
    if n == 0:
        return M_add({x: size}, get_state({x: 0}, f), f)
    else:
        m = max(0, n - 1)
        return M_add({x: m}, get_state({x: n}, f), rshift_prime(m, size, f, x))


def rshift(f, x, n):
    return rshift_prime(max_helper(n, 1), max_helper(n, 1), f, x)


def reverse_prime(f, x, n, i, f_prime):
    if n == 0:
        return f_prime
    else:
        i_prime = max(0, n - 1)
        return reverse_prime(f, x, n, i_prime,
                             M_add(
                                 {x: i_prime},
                                 get_state({x: max_helper(n, i)}, f),
                                 f_prime)
                             )


def reverse(f, x, n):
    return reverse_prime(f, x, n, n, f)


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


def turn_qft(f, x, n, rmax):
    assign_h(
        assign_r(
            f, x,
            (2 ** max_helper(rmax, n)) * a_nat2fb(fbrev(n, get_cus(n, f, x)), n),
            n, n, rmax
        ),
        x, n, max_helper(rmax, n), rmax
    )


# TODO implement
def turn_rqft(st, x, n, rmax):
    pass


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


"""
Simulator class
  This class extends ExpVisitor, and is essentially an interpreter
  for the OCAML code that we will be testing.
  Follows visitor pattern.
"""


class Simulator(ExpVisitor):

    def __init__(self, st: ChainMap, env, rmax):
        self.st = st
        self.env = env
        self.rmax = rmax

    def visitSkipexp(self, ctx: SkipexpContext):
        return self.st

    def visitXgexp(self, ctx: XgexpContext):
        p = ctx.e
        M_add(p, exchange(get_state(p, self.st)), self.st)

    def visitCUexp(self, ctx: CuexpContext):
        p = ctx.e1
        e_prime = ctx.e2
        if get_cua(get_state(p, self.st)):
            self.visit(e_prime)
        else:
            return self.st

    def visitRzexp(self, ctx: RzexpContext):
        q = ctx.e1
        p = ctx.e2
        M_add(p, times_rotate(get_state(p, self.st), q, self.rmax), self.st)

    def visitRrzexp(self, ctx: RrzexpContext):
        q = ctx.e1
        p = ctx.e2
        M_add(p, times_r_rotate(get_state(p, self.st), q, self.rmax), self.st)

    def visitSrexp(self, ctx: SrexpContext):
        n = ctx.e1
        x = ctx.e2
        sr_rotate(self.st, x, n, self.rmax)

    def visitSrrexp(self, ctx: SrrexpContext):
        n = ctx.e1
        x = ctx.e2
        srr_rotate(self.st, x, n, self.rmax)

    def visitLshiftexp(self, ctx: LshiftexpContext):
        x = ctx.e1
        lshift(self.st, x, self.env(x))

    def visitRshiftexp(self, ctx: RshiftexpContext):
        x = ctx.e1
        rshift(self.st, x, self.env(x))

    def visitRevexp(self, ctx: RevexpContext):
        x = ctx.e1
        reverse(self.st, x, self.env(x))

    def visitQftexp(self, ctx: QftexpContext):
        x = ctx.e1
        turn_qft(self.st, x, self.env(x), self.rmax)

    def visitRqftexp(self, ctx: RqftexpContext):
        x = ctx.e1
        turn_rqft(self.st, x, self.env(x), self.rmax)

    def visitSeqexp(self, ctx: SeqexpContext):
        e1 = ctx.e1
        e2 = ctx.e2
        self.visit(e1)
        self.visit(e2)

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            self.visitChildren(ctx)
        else:
            self.visitTerminal(ctx)

    def visitChildren(self, ctx: ParserRuleContext):
        for child in ctx.children:
            self.visit(child)

    def visitTerminal(self, node: ParserRuleContext):
        if isinstance(node, SkipexpContext):
            self.visitSkipexp(node)
        elif isinstance(node, XgexpContext):
            self.visitXgexp(node)
        elif isinstance(node, CuexpContext):
            self.visitCUexp(node)
        elif isinstance(node, RzexpContext):
            self.visitRzexp(node)
        elif isinstance(node, RrzexpContext):
            self.visitRrzexp(node)
        elif isinstance(node, SrexpContext):
            self.visitSrexp(node)
        elif isinstance(node, SrrexpContext):
            self.visitSrrexp(node)
        elif isinstance(node, LshiftexpContext):
            self.visitLshiftexp(node)
        elif isinstance(node, RshiftexpContext):
            self.visitRshiftexp(node)
        elif isinstance(node, RevexpContext):
            self.visitRevexp(node)
        elif isinstance(node, QftexpContext):
            self.visitQftexp(node)
        elif isinstance(node, RqftexpContext):
            self.visitRqftexp(node)
        elif isinstance(node, SeqexpContext):
            self.visitSeqexp(node)
