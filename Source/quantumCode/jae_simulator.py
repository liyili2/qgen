from AST_Scripts.ExpParser import *
import simulator


# Copying verbatim code from Testing.ml
# Instead of an expression e, we pass in a context (ctx)
#   which contains at least one expression, e

def visitSkipexp(self, ctx: SkipexpContext, st):
    return st


# TODO: XgexpContext does not currently exist.
def visitXgexp(self, ctx: XgexpContext, st, env, rmax):
    p = ctx.e
    return M.add(p, simulator.exchange(simulator.get_state(p, st)), st)


# TODO: find out why `p` is giving a warning
def visitCUexp(self, ctx: CuexpContext, st, env, rmax):
    p = ctx.e1
    e2 = ctx.e2
    if simulator.get_cua(simulator.get_state(p, st)):
        pass
    else:
        return st


# TODO implement M
def visitRzexp(self, ctx: RzexpContext, st, env, rmax):
    q = ctx.e1
    p = ctx.e2
    M.add(p, simulator.times_rotate(simulator.get_state(p, st), q, rmax), st)


def visitRrzexp(self, ctx: RrzexpContext, st, env, rmax):
    q = ctx.e1
    p = ctx.e2
    M.add(p, simulator.times_r_rotate(simulator.get_state(p, st), q, rmax), st)


def visitSrexp(self, ctx: SrexpContext, st, env, rmax):
    n = e1
    x = e2
    return simulator.sr_rotate(st, x, n, rmax)


def visitSrrexp(self, ctx: SrrexpContext, st, env, rmax):
    n = ctx.e1
    x = ctx.e2
    return simulator.srr_rotate(st, x, n, rmax)


def visitLshiftexp(self, ctx: LshiftexpContext, st, env, rmax):
    x = ctx.e1
    return simulator.lshift(st, x, env(x)) # TODO verify this matches VQO code


def visitRshiftexp(self, ctx: RshiftexpContext, st, env, rmax):
    x = ctx.e1
    return simulator.rshift(st, x, env(x))


def visitRevexp(self, ctx: RevexpContext, st, env, rmax):
    x = ctx.e1
    return simulator.reverse(st, x, env(x))


def visitQftexp(self, ctx: QftexpContext, st, env, rmax):
    x = ctx.e1
    return simulator.turn_qft(st, x, env(x), rmax)


def visitRqftexp(self, ctx: RqftexpContext, st, env, rmax):
    x = ctx.e1
    return simulator.turn_rqft(st, x, env(x), rmax)


def visitSeqexp(self, ctx: SeqexpContext, st, env, rmax):
    e1 = ctx.e1
    e2 = ctx.e2
    pass