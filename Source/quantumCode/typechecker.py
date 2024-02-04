# type checker
from enum import Enum


class TypeName:
    pass  # TODO


class Nor(TypeName):

    def __init__(self):


class QFT(TypeName):

    def __init__(self, n: int):
        self.n = n
        #self.r2 = r2


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


class TypeChecker(ExpVisitor):

    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, tenv: ChainMap, env: ChainMap):
        self.tenv = tenv
        self.env = env
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    # define posi to be a pair of string,int
    def visitPosiexp(self, ctx: ExpParser.PosiexpContext):
        name = ctx.vexp(0).accept(self)
        num = int(ctx.vexp(1).accept(self))
        return name, num

    # should do nothing
    def visitSkipexp(self, ctx: ExpParser.SkipexpContext):
        return True

    # X posi, changed the following for an example
    def visitXgexp(self, ctx: ExpParser.XgexpContext):
        x, p = ctx.posiexp().accept(self)  # this will pass the visitor to the child of ctx
        return isinstance(M_find(x, self.tenv), Nor) and 0 <= p < M_find(x, self.env)

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: ExpParser.CuexpContext):
        x, p = ctx.posiexp().accept(self)
        if isinstance(M_find(x, self.tenv), Nor) and 0 <= p < M_find(x, self.env):
            ctx.exp().accept(self)
        else:
            return False

    # my previous rz parsing is wrong
    # it should be RZ q posi
    def visitRzexp(self, ctx: ExpParser.RzexpContext):
        q = int(ctx.vexp().accept(self))  # I guess then you need to define vexp
        # we can first define the var and integer case
        # I guess Identifier and int are all terminal
        # does it means that we do not need to define anything?
        x, p = ctx.posiexp().accept(self)
        return isinstance(M_find(x, self.tenv), Nor) and 0 <= p < M_find(x, self.env) and 0 <= abs(q) <= M_find(x, self.tenv).n

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: ExpParser.SrexpContext):
        b = int(ctx.vexp(0).accept(self))
        x = ctx.vexp(1).accept(self)
        return isinstance(M_find(x, self.tenv), QFT) and 0 <= abs(b) <= M_find(x, self.tenv).n

    def visitLshiftexp(self, ctx: ExpParser.LshiftexpContext):
        x = ctx.vexp().accept(self)
        return isinstance(M_find(x, self.tenv),Nor)

    def visitRshiftexp(self, ctx: ExpParser.RshiftexpContext):
        x = ctx.vexp().accept(self)
        return isinstance(M_find(x, self.tenv),Nor)

    def visitRevexp(self, ctx: ExpParser.RevexpContext):
        x = ctx.vexp().accept(self)
        return isinstance(M_find(x, self.tenv),Nor)

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: ExpParser.QftexpContext):
        x = ctx.vexp(0).accept(self)
        b = int(ctx.vexp(1).accept(self))
        if isinstance(M_find(x, self.tenv), Nor) and 0 <= b <= M_find(x, self.env):
            M_add(x, QFT(M_find(x,self.env) - b), self.tenv)
            return True
        return False

    def visitRqftexp(self, ctx: ExpParser.RqftexpContext):
        x = ctx.vexp(0).accept(self)
        b = int(ctx.vexp(1).accept(self))
        if isinstance(M_find(x, self.tenv), QFT) and b + M_find(x, self.tenv).n == M_find(x, self.env):
            M_add(x, Nor, self.tenv)
            return True
        return False

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
