# type checker
import copy
from enum import Enum
from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from Source.quantumCode.AST_Scripts.BlockContain import BlockContain
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser
from Source.quantumCode.AST_Scripts.XMLExpVisitor import XMLExpVisitor
from Source.quantumCode.AST_Scripts.XMLTypeSearch import Qty, joinType, Nat


class TypeDetector(XMLExpVisitor):

    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, type_environment: dict):
        self.type_environment = type_environment
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        while ctx.exp(i) is not None:
            if ctx.exp(i).blockexp() is not None:
                return
            else:
                ctx.exp(i).accept(self)
            i += 1

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        ctx.program().accept(self)

    def visitExp(self, ctx: XMLExpParser.ExpContext):
        if ctx.letexp() is not None:
            ctx.letexp().accept(self)
        elif ctx.appexp() is not None:
            ctx.appexp().accept(self)
        elif ctx.ifexp() is not None:
            ctx.ifexp().accept(self)
        elif ctx.matchexp() is not None:
            ctx.matchexp().accept(self)
        elif ctx.cuexp() is not None:
            self.visitCUexp(ctx.cuexp())
        elif ctx.skipexp() is not None:
            ctx.skipexp().accept(self)
        elif ctx.xexp() is not None:
            ctx.xexp().accept(self)
        elif ctx.srexp() is not None:
            ctx.srexp().accept(self)
        elif ctx.qftexp() is not None:
            ctx.qftexp().accept(self)
        elif ctx.lshiftexp() is not None:
            ctx.lshiftexp().accept(self)
        elif ctx.rshiftexp() is not None:
            ctx.rshiftexp().accept(self)
        elif ctx.revexp() is not None:
            ctx.revexp().accept(self)
        elif ctx.rqftexp() is not None:
            ctx.rqftexp().accept(self)
        elif ctx.blockexp() is not None:
            ctx.blockexp().accept(self)

    def get_type_env(self):
        return self.type_environment

    def visitElement(self, ctx: XMLExpParser.ElementContext):
        if ctx.numexp() is not None:
            return str(ctx.numexp().accept(self))
        else:
            tv = ctx.Identifier().accept(self)
            if isinstance(self.type_environment.get(tv), Nat()):
                return tv

    def visitAtype(self, ctx: XMLExpParser.AtypeContext):
        if ctx.Nat() is not None:
            return Nat()
        elif ctx.Qt() is not None:
            return Qty(ctx.element(0).accept(self))
        elif ctx.Nor() is not None:
            return Qty(ctx.element(0).accept(self), "Nor")
        elif ctx.Phi() is not None:
            return Qty(ctx.element(0).accept(self), "Phi", ctx.element(1).accept(self))

    def visitLetexp(self, ctx: XMLExpParser.LetexpContext):
        bl = BlockContain()
        if bl.visitProgram(ctx.program()):
            i = 0
            f = ctx.Identifier().accept(self)
            tml = []
            tmv = copy.deepcopy(self.type_environment)
            while ctx.idexp(i) is not None:
                x = ctx.idexp(i).Identifier().accept(self)
                tml.append(x)
                v = ctx.idexp(i).atype().accept(self)
                self.type_environment.update({x: v})
                i += 1
            ctx.program().accept(self)
            #tmv.update({f: Fun(tml, tx.type_environment, self.type_environment)})

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        identifier_text = ctx.Identifier().accept(self)
        qty = self.type_environment.get(identifier_text)
        tml = qty.args
        tmv = qty.pre
        rmv = qty.out
        for i in range(len(tml)):
            if ctx.vexp(i).idexp() is not None:
                na = ctx.vexp(i).idexp().Identifier().accept(self)
                tmpty = self.type_environment.get(na)
                tx = joinType(tmv.get(tml[i]), tmpty)
                if tx is None:
                    return
                self.type_environment.update({na: rmv.get(tml[i])})

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        bl = BlockContain()
        if bl.visitProgram(ctx.exppair(0).program()):
            ctx.exppair(0).program().accept(self)
        elif bl.visitProgram(ctx.exppair(1).program()):
            va = ctx.exppair(1).element().Identifier().accept(self)
            self.type_environment.update({va: Nat()})
            ctx.exppair(1).program().accept(self)
            self.type_environment.pop(va)

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        return

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Nor")})
                return
        #return p < self.env.get(x) and str(self.type_environment.get(x)) == "Nor"
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Nor")})
                ctx.program().accept(self)
            else:
                ctx.program().accept(self)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Phi")})

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Nor")})

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Nor")})

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Nor")})

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.Identifier().accept(self)
        ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            temp = (self.type_environment.get(x))
            print(temp)
            if temp.type is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Phi")})
            elif self.type_environment.get(x).type() == "Nor":
                self.type_environment.update({x: Qty(self.type_environment.get(x).get_num(), "Phi")})


    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.update({x:Qty(self.type_environment.get(x).get_num(),"Nor")})
            elif self.type_environment.get(x).type() == "Phi":
                self.type_environment.update({x: Qty(self.type_environment.get(x).get_num(), "Nor")})

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            self.visitChildren(ctx)
        else:
            self.visitTerminal(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        return isinstance(self.type_environment.get(ctx.Identifier().accept(self)), Nat)

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
