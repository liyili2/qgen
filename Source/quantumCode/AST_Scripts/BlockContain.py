# type checker
import copy
from enum import Enum
from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from XMLExpParser import *
from XMLExpVisitor import *

class BlockContain(XMLExpVisitor):

    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self):
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        tmp = False
        while ctx.exp(i) is not None:
            tmp = tmp or ctx.exp(i).accept(self)
            i += 1
        return tmp

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        return ctx.program().accept(self)

    def visitExp(self, ctx: XMLExpParser.ExpContext):
        if ctx.appexp() is not None:
            return ctx.appexp().accept(self)
        elif ctx.ifexp() is not None:
            return ctx.ifexp().accept(self)
        elif ctx.cuexp() is not None:
            return self.visitCUexp(ctx.cuexp())
        elif ctx.skipexp() is not None:
            return ctx.skipexp().accept(self)
        elif ctx.xexp() is not None:
            return ctx.xexp().accept(self)
        elif ctx.srexp() is not None:
            return ctx.srexp().accept(self)
        elif ctx.qftexp() is not None:
            return ctx.qftexp().accept(self)
        elif ctx.lshiftexp() is not None:
            return ctx.lshiftexp().accept(self)
        elif ctx.rshiftexp() is not None:
            return ctx.rshiftexp().accept(self)
        elif ctx.revexp() is not None:
            return ctx.revexp().accept(self)
        elif ctx.rqftexp() is not None:
            return ctx.rqftexp().accept(self)
        elif ctx.blockexp() is not None:
            return ctx.blockexp().accept(self)

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        vx = ctx.Identifier().accept(self)
        qty = self.type_environment.get(vx)
        tml = qty.args()
        tmv = qty.pre()
        rmv = qty.out()
        tmp = True
        for i in range(len(tml)):
            if ctx.vexp(i).idexp() is not None:
                na = ctx.vexp(i).idexp().Identifier().accept(self)
                tmpty = self.type_environment.get(na)
                tx = joinType(tmv.get(tml[i]), tmpty)
                if tx is None:
                    return False
                self.type_environment.update({na: rmv.get(tml[i])})
            else:
                tmp = tmp and ctx.vexp(i).accept(self)
        return tmp

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        return ctx.exppair(0).program().accept(self) and ctx.exppair(1).program().accept(self)

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        return ctx.nextexp(0).accept(self) and ctx.nextexp(1).accept(self)

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        return False

    def visitBlockexp(self, ctx: XMLExpParser.BlockexpContext):
        return True

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        return False

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        return False

        #return p < self.env.get(x) and str(self.type_environment.get(x)) == "Nor"
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        return ctx.program().accept(self)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        return False

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        return False

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        return False

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        return False

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        return False

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        return False
