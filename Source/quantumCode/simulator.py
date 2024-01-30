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
        #128
        #may array x, y, z, u, v
        #st: x[0] -> bit / phase n e^{2 pi i * 1/ n}
        self.st = st
        self.env = env
        self.rmax = rmax

   #define posi to be a pair of string,int
    def visitPosiexp(self, ctx:ExpParser.PosiexpContext):
        name = ctx.vexp(0).accept(self)
        num = int(ctx.vexp(1).accept(self))
        return name,num

    #should do nothing
    def visitSkipexp(self, ctx: ExpParser.SkipexpContext):
        return

   #X posi, changed the following for an example
    def visitXgexp(self, ctx: ExpParser.XgexpContext):
        #p = self.visit(ctx) # I doubt this will work. maybe the following
        p = ctx.posiexp().accept(self) #this will pass the visitor to the child of ctx
        self.st = M_add(p, exchange(get_state(p, self.st)), self.st)

    #we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: ExpParser.CuexpContext):
        p = ctx.posiexp().accept(self)
        if get_cua(get_state(p, self.st)):
            ctx.exp().accept(self)
        else:
            return # do nothing

    #my previous rz parsing is wrong
    # it should be RZ q posi
    def visitRzexp(self, ctx: ExpParser.RzexpContext):
        q = int(ctx.vexp().accept(self)) #I guess then you need to define vexp
                                         # we can first define the var and integer case
                                         #I guess Identifier and int are all terminal
                                         #does it means that we do not need to define anything?
        p = ctx.posiexp().accept(self)
        st = M_add(p, times_rotate(get_state(p, self.st), q, self.rmax), self.st)

    def visitRrzexp(self, ctx: ExpParser.RrzexpContext):
        q = int(ctx.vexp().accept(self))
        p = ctx.posiexp().accept(self)
        #p = out[1]
        st = M_add(p, times_r_rotate(get_state(p, self.st), q, self.rmax), self.st)

    #SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: ExpParser.SrexpContext):
        n = int(ctx.vexp(0).accept(self))
        x = ctx.vexp(1).accept(self)
        st = sr_rotate(self.st, x, n, self.rmax)

    def visitSrrexp(self, ctx: ExpParser.SrrexpContext):
        n = int(ctx.vexp(0).accept(self))
        x = ctx.vexp(1).accept(self)
        return srr_rotate(self.st, x, n, self.rmax)

    def visitLshiftexp(self, ctx: ExpParser.LshiftexpContext):
        x = ctx.vexp().accept(self)
        return lshift(self.st, x, self.env(x))

    def visitRshiftexp(self, ctx: ExpParser.RshiftexpContext):
        x = ctx.vexp().accept(self)
        return rshift(self.st, x, self.env(x))

    def visitRevexp(self, ctx: ExpParser.RevexpContext):
        x = ctx.vexp().accept(self)
        return reverse(self.st, x, self.env(x))

    #actually, we need to change the QFT function
    #the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: ExpParser.QftexpContext):
        x = ctx.vexp(0).accept(self)
        b = int(ctx.vexp(1).accept(self))
        return turn_qft(self.st, x, b, self.rmax)

    def visitRqftexp(self, ctx: ExpParser.RqftexpContext):
        x = ctx.vexp(0).accept(self)
        b = int(ctx.vexp(1).accept(self))
        return turn_rqft(self.st, x, b, self.rmax)

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

    #the only thing that matters will be 48 and 47
    def visitTerminal(self, node):
        if node.getSymbol().type == ExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == ExpParser.Number:
            return node.getText()
        return "None"
