# type checker
import copy
from enum import Enum
from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from quantumCode.AST_Scripts.XMLExpLexer import *
from quantumCode.AST_Scripts.XMLExpVisitor import *
from quantumCode.AST_Scripts.XMLTypeSearch import *
from quantumCode.AST_Scripts.XMLProgrammer import *

class ProgramTransformer(XMLExpVisitor):

    def visitRoot(self, ctx: XMLExpParser.RootContext):
        program = ctx.program().accept(self)
        return QXRoot(program)

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        tmp = []
        while ctx.exp(i) is not None:
            tmp = tmp.append(ctx.exp(i).accept(self))
            i += 1
        return QXProgram(tmp)

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        return QXNext(ctx.program().accept(self))

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
        return self.type_environment

    def visitElement(self, ctx: XMLExpParser.ElementContext):
        if ctx.numexp() is not None:
            return QXNum(ctx.numexp().accept(self))
        else:
            return QXIDExp(ctx.Identifier().accept(self), None)

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
            x = ctx.idexp(i).accept(self)
            tml.append(x)
        fv = ctx.program().accept(self)
        return QXLet(f, tml, fv)

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        f = ctx.vexp().accept(self)
        left = ctx.nextexp(0).accept(self)
        right = ctx.nextexp(1).accept(self)
        return QXIf(f,left,right)

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        vx = ctx.Identifier().accept(self)
        i = 0
        tmp = []
        while ctx.vexp(i) is not None:
            tmp.append(ctx.vexp(i).accep(self))
        return QXApp(vx,tmp)

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        x = ctx.Identifier().accept(self)
        left = ctx.exppair(0).accept(self)
        right = ctx.exppair(1).accept(self)
        return QXMatch(x,left, right)

    def visitExppair(self, ctx:XMLExpParser.ExppairContext):
        elem = ctx.element().accept(self)
        prog = ctx.program().accept(self)
        return QXPair(elem, prog)

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        x = ctx.Identifier().accept(self)
        v = ctx.vexp().accept(self)
        return QXSKIP(x, v)

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.Identifier().accept(self)
        v = ctx.vexp().accept(self)
        return QXX(x, v)

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.Identifier().accept(self)
        v = ctx.vexp().accept(self)
        p = ctx.program().accept(self)
        return QXCU(x, v, p)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        x = ctx.Identifier().accept(self)
        v = ctx.vexp().accept(self)
        return QXSR(x, v)

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.Identifier().accept(self)
        return QXLshift(x)

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.Identifier().accept(self)
        return QXRshift(x)

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.Identifier().accept(self)
        return QXRev(x)

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.Identifier().accept(self)
        v = ctx.vexp().accept(self)
        return QXQFT(x,v)


    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.Identifier().accept(self)
        return QXRQFT(x)

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        x = ctx.Identifier().accept(self)
        t = ctx.atype().accept(self)
        return QXIdExp(x, t)

    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.idexp() is not None:
            return ctx.idexp().accept(self)
        if ctx.NUM() is not None:
            v = ctx.numexp().accept(self)
            return QXNum(v)
        else:
            return QXBin(str(ctx.OP()), ctx.vexp(0).accept(self), ctx.vexp(1).accept(self))
    # the only thing that matters will be 48 and 47

    def visitAtype(self, ctx:XMLExpParser.AtypeContext):
        if ctx.Nat() is not None:
            return Nat()
        if ctx.Qt() is not None:
            v = ctx.element(0).accept(self)
            return Qty(v)
        if ctx.Nor() is not None:
            v = ctx.element(0).accept(self)
            return Qty(v, "Nor")
        if ctx.Nor() is not None:
            v = ctx.element(0).accept(self)
            v1 = ctx.element(1).accept(self)
            return Qty(v, "Phi", v1)

    def visitTerminal(self, node):
        # print("terminal")
        if node.getSymbol().type == XMLExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == XMLExpParser.Number:
            return int(node.getText())
        return "None"
