import collections

from AST_Scripts.ExpParser import *
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
    pass  # TODO implement


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
    return (r + 2 ** addto_helper(rmax, n)) % 2 ** rmax


def addto_helper(x, y):
    return x - y if x - y > 0 else 0


def rotate(r, n, rmax):
    return addto(r, n, rmax)


def addto_n(r, n, rmax):
    return addto_helper(r + 2 ** rmax, 2 ** addto_helper(rmax, n)) % 2 ** rmax


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
        m = 0 if 0 > n - 1 else n - 1
        return sr_rotate_prime()  # TODO finish


def sr_rotate(st, x, n, rmax):
    return sr_rotate_prime(st, x, n + 1, n + 1, rmax)


# Essentially works as M.add from Testing.ml
# TODO ensure we aren't losing any behavior
def update_map(M: collections.ChainMap, key, value):
    M.maps[0][key] = value


"""
Simulator class
  This class extends ExpVisitor, and is essentially an interpreter
  for the OCAML code that we will be testing.
  Follows visitor pattern.
"""


class Simulator(ExpVisitor):

    def __init__(self, st, env, rmax, M: collections.ChainMap):
        self.st = st
        self.env = env
        self.rmax = rmax
        self.M = M

    def visitSkipexp(self, ctx: SkipexpContext):
        return self.st

    # TODO: XgexpContext does not currently exist.
    def visitXgexp(self, ctx: XgexpContext):
        p = ctx.e
        update_map(self.M, p, exchange(get_state(p, self.st)))

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
        update_map(self.M, p, times_rotate(get_state(p, self.st), q, self.rmax))

    def visitRrzexp(self, ctx: RrzexpContext):
        q = ctx.e1
        p = ctx.e2
        update_map(self.M, p, times_r_rotate(get_state(p, self.st), q, self.rmax))

    def visitSrexp(self, ctx: SrexpContext):
        n = ctx.e1
        x = ctx.e2
        sr_rotate(self.st, x, n, self.rmax)

    # TODO implement srr_rotate
    def visitSrrexp(self, ctx: SrrexpContext):
        n = ctx.e1
        x = ctx.e2
        srr_rotate(self.st, x, n, self.rmax)

    # TODO verify that lshift is correct method
    def visitLshiftexp(self, ctx: LshiftexpContext):
        x = ctx.e1
        lshift(self.st, x, self.env(x))  # TODO verify that env is a method

    # TODO verify that rshift is correct method
    def visitRshiftexp(self, ctx: RshiftexpContext):
        x = ctx.e1
        rshift(self.st, x, self.env(x))

    # TODO implement reverse()
    def visitRevexp(self, ctx: RevexpContext):
        x = ctx.e1
        reverse(self.st, x, self.env(x))

    # TODO implement turn_qft()
    def visitQftexp(self, ctx: QftexpContext):
        x = ctx.e1
        turn_qft(self.st, x, self.env(x), self.rmax)

    # TODO implement turn_rqft()
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
