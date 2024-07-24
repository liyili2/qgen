# type checker
import copy
from enum import Enum
from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from XMLExpParser import *
from XMLExpVisitor import *
from XMLTypeSearch import *


class TypeInfer(XMLExpVisitor):

    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, tenv: dict):
        self.tenv = tenv
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitRoot(self, ctx: XMLExpParser.RootContext):
        return ctx.program().accept(self)

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        tmp = True
        while ctx.exp(i) is not None:
            tmp = tmp and ctx.exp(i).accept(self)
            i += 1
        return tmp

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        return ctx.program().accept(self)

    def visitExp(self, ctx: XMLExpParser.ExpContext):
        if ctx.letexp() is not None:
            return ctx.letexp().accept(self)
        elif ctx.appexp() is not None:
            return ctx.appexp().accept(self)
        elif ctx.ifexp() is not None:
            return ctx.ifexp().accept(self)
        elif ctx.matchexp() is not None:
            return ctx.matchexp().accept(self)
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

    def get_type_env(self):
        return self.tenv

    def visitElement(self, ctx: XMLExpParser.ElementContext):
        if ctx.numexp() is not None:
            return ctx.numexp().accept(self)
        else:
            return ctx.Identifier().accept(self)

    def visitAtype(self, ctx: XMLExpParser.AtypeContext):
        if ctx.Nat() is not None:
            return Nat()
        elif ctx.Qt() is not None:
            return Qty(ctx.element(0).accept(self))
        elif ctx.Nor() is not None:
            return Qty(ctx.element(0).accept(self), "Nor")
        elif ctx.Phi() is not None:
            return Qty(ctx.element(0).accept(self), "Phi", ctx.element(1).accept(self))
        return Nat()

    def visitLetexp(self, ctx: XMLExpParser.LetexpContext):
        i = 0
        f = ctx.Identifier().accept(self)
        tml = []
        while ctx.idexp(i) is not None:
            x = ctx.idexp(i).Identifier().accept(self)
            tml.append(x)
            v = ctx.idexp(i).atype().accept(self)
            self.tenv.update({x: v})
            i += 1

        tmv = copy.deepcopy(self.tenv)
        tx = TypeSearch(self.tenv)
        tx.visitProgram(ctx.program())
        self.tenv = copy.deepcopy(tx.tenv)
        fv = ctx.program().accept(self)
        tmv.update({f: Fun(tml, tx.tenv, self.tenv)})

        for j in range(len(tml)):
            tmv.pop(tml[j])
            j += 1
        self.tenv = tmv
        return fv
        #print("f", ctx)
        #ctx.exp().accept(self)

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        if ctx.vexp().accept(self):
            tmv = copy.deepcopy(self.tenv)
            tmp1 = ctx.nextexp(0).accept(self)
            rmv = copy.deepcopy(self.tenv)
            self.tenv = tmv
            tmp2 = ctx.nextexp(1).accept(self)
            return tmp1 and tmp2 and equalTypes(rmv, self.tenv)
        return False

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        vx = ctx.Identifier().accept(self)
        qty = self.tenv.get(vx)
        tml = qty.args()
        tmv = qty.pre()
        rmv = qty.out()
        tmp = True
        for i in range(len(tml)):
            if ctx.vexp(i).idexp() is not None:
                na = ctx.vexp(i).idexp().Identifier().accept(self)
                tmpty = self.tenv.get(na)
                tx = joinType(tmv.get(tml[i]), tmpty)
                if tx is None:
                    return False
                self.tenv.update({na: rmv.get(tml[i])})
            else:
                tmp = tmp and ctx.vexp(i).accept(self)
        return tmp

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        x = ctx.Identifier().accept(self)
        #value = self.st.get(x)
        #print("value match", value)
        fenv = copy.deepcopy(self.tenv)
        va = ctx.exppair(1).element().Identifier().accept(self)
        senv = copy.deepcopy(self.tenv)
        senv.update({va: Nat()})
        s1 = TypeSearch(fenv)
        s1.visitProgram(ctx.exppair(0).program())
        s2 = TypeSearch(senv)
        s2.visitProgram(ctx.exppair(1).program())
        fenv1 = s1.tenv
        senv1 = s2.tenv.pop(va)
        senv2 = joinTypes(fenv1, senv1)
        fenv3 = copy.deepcopy(senv2)
        self.tenv = fenv3
        ctx.exppair(0).program().accept(self)
        fenv4 = self.tenv
        self.tenv = senv2.update({va: Nat()})
        ctx.exppair(1).program().accept(self)
        senv3 = self.tenv
        return equalTypes(fenv4,senv3.pop(va))

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        return isinstance(self.tenv.get(x), Qty)

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Nor")})
                return True
            else:
                return self.tenv.get(x).type() == "Nor"
        return False
        #return p < self.env.get(x) and str(self.tenv.get(x)) == "Nor"
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Nor")})
                ctx.program().accept(self)
                return True
            else:
                ctx.program().accept(self)
                return self.tenv.get(x).type() == "Nor"
        return False

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Phi")})
                return True
            else:
                return self.tenv.get(x).type() == "Phi"
        return False

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Nor")})
                return True
            else:
                return self.tenv.get(x).type() == "Nor"
        return False

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Nor")})
                return True
            else:
                return self.tenv.get(x).type() == "Nor"
        return False

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Nor")})
                return True
            else:
                return self.tenv.get(x).type() == "Nor"
        return False

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Phi")})
                return True
            elif self.tenv.get(x).type() == "Nor":
                self.tenv.update({x: Qty(self.tenv.get(x).get_num(), "Phi")})
                return True
        return False


    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.update({x:Qty(self.tenv.get(x).get_num(),"Nor")})
                return True
            elif self.tenv.get(x).type() == "Phi":
                self.tenv.update({x: Qty(self.tenv.get(x).get_num(), "Nor")})
                return True
        return False

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        return isinstance(self.tenv.get(ctx.Identifier().accept(self)), Nat)

    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.idexp() is not None:
            return ctx.idexp().accept(self)
        if ctx.NUM() is not None:
            return True
        else:
            #print("here")
            #print("op",ctx.op())
            return ctx.vexp(0).accept(self) and ctx.vexp(1).accept(self)
    # the only thing that matters will be 48 and 47

    def visitTerminal(self, node):
        # print("terminal")
        if node.getSymbol().type == XMLExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == XMLExpParser.Number:
            return int(node.getText())
        return "None"
