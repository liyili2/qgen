import collections

from AST_Scripts.ExpParser import *
from Source.quantumCode.AST_Scripts.ExpVisitor import ExpVisitor

"""
Helper Functions
"""


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
    # TODO: implement exchange and get_state
    def visitXgexp(self, ctx: XgexpContext):
        p = ctx.e
        update_map(self.M, p, exchange(get_state(p, self.st)))

    # TODO implement get_cua
    def visitCUexp(self, ctx: CuexpContext):
        p = ctx.e1
        e_prime = ctx.e2
        if get_cua(get_state(p, self.st)):
            pass  # TODO visit on e_prime
        else:
            return self.st

    # TODO implement times_rotate
    def visitRzexp(self, ctx: RzexpContext):
        q = ctx.e1
        p = ctx.e2
        update_map(self.M, p, times_rotate(get_state(p, self.st), q, self.rmax))

    # TODO implement times_r_rotate
    def visitRrzexp(self, ctx: RrzexpContext):
        q = ctx.e1
        p = ctx.e2
        update_map(self.M, p, times_r_rotate(get_state(p, self.st), q, self.rmax))

    # TODO implement sr_rotate
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
        pass  # TODO visit e1 and e2
