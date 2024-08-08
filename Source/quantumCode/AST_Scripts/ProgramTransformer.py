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
        program = self.visitProgram(ctx.program())
        return QXRoot(program)

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        tmp = []
        while ctx.exp(i) is not None:
            v = self.visitExp(ctx.exp(i))
            tmp.append(v)
            i += 1
        return QXProgram(tmp)

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        v = self.visitProgram(ctx.program())
        return QXNext(v)

    def visitExp(self, ctx: XMLExpParser.ExpContext):
        if ctx.letexp() is not None:
            return self.visitLetexp(ctx.letexp())
        elif ctx.appexp() is not None:
            return self.visitAppexp(ctx.appexp())
        elif ctx.ifexp() is not None:
            return self.visitIfexp(ctx.ifexp())
        elif ctx.matchexp() is not None:
            return self.visitMatchexp(ctx.matchexp())
        elif ctx.cuexp() is not None:
            return self.visitCUexp(ctx.cuexp())
        elif ctx.skipexp() is not None:
            return self.visitSkipexp(ctx.skipexp())
        elif ctx.xexp() is not None:
            return self.visitXexp(ctx.xexp())
        elif ctx.srexp() is not None:
            return self.visitSrexp(ctx.srexp())
        elif ctx.qftexp() is not None:
            return self.visitQftexp(ctx.qftexp())
        elif ctx.lshiftexp() is not None:
            return self.visitLshiftexp(ctx.lshiftexp())
        elif ctx.rshiftexp() is not None:
            return self.visitRshiftexp(ctx.rshiftexp())
        elif ctx.revexp() is not None:
            return self.visitRevexp(ctx.revexp())
        elif ctx.rqftexp() is not None:
            return self.visitRqftexp(ctx.rqftexp())
        elif ctx.blockexp() is not None:
            return self.visitBlockexp(ctx.blockexp())

    def get_type_env(self):
        return self.type_environment

    def visitElement(self, ctx: XMLExpParser.ElementContext):
        if ctx.numexp() is not None:
            v = self.visitNumexp(ctx.numexp())
            return QXNum(v)
        else:
            return QXIDExp(ctx.Identifier(), None)

    def visitAtype(self, ctx: XMLExpParser.AtypeContext):
        if ctx.Nat() is not None:
            return Nat()
        elif ctx.Qt() is not None:
            v = self.visitElement(ctx.element(0))
            return Qty(v)
        elif ctx.Nor() is not None:
            v = self.visitElement(ctx.element(0))
            return Qty(v, "Nor")
        elif ctx.Phi() is not None:
            v = self.visitElement(ctx.element(0))
            v1 = v = self.visitElement(ctx.element(1))
            return Qty(v, "Phi", v1)
        return Nat()

    def visitLetexp(self, ctx: XMLExpParser.LetexpContext):
        i = 0
        f = ctx.Identifier()
        tml = []
        while ctx.idexp(i) is not None:
            x = self.visitIdexp(ctx.idexp(i))
            tml.append(x)
            i += 1
        fv = self.visitProgram(ctx.program())
        return QXLet(f, tml, fv)

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        f = self.visitVexp(ctx.vexp())
        left = self.visitNextexp(ctx.nextexp(0))
        right = self.visitNextexp(ctx.nextexp(1))
        return QXIf(f,left,right)

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        vx = ctx.Identifier()
        i = 0
        tmp = []
        while ctx.vexp(i) is not None:
            v = self.visitVexp(ctx.vexp(i))
            tmp.append(v)
            i = i + 1
        return QXApp(vx,tmp)

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        x = ctx.Identifier()
        left = self.visitExppair(ctx.exppair(0))
        right = self.visitExppair(ctx.exppair(1))
        return QXMatch(x,left, right)

    def visitExppair(self, ctx:XMLExpParser.ExppairContext):
        elem = self.visitElement(ctx.element())
        prog = self.visitProgram(ctx.program())
        return QXPair(elem, prog)

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        x = ctx.Identifier()
        v = self.visitVexp(ctx.vexp())
        return QXSKIP(x, v)

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.Identifier()
        v = self.visitVexp(ctx.vexp())
        return QXX(x, v)

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.Identifier()
        v = self.visitVexp(ctx.vexp())
        p = self.visitProgram(ctx.program())
        return QXCU(x, v, p)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        x = ctx.Identifier()
        v = self.visitVexp(ctx.vexp())
        return QXSR(x, v)

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.Identifier()
        return QXLshift(x)

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.Identifier()
        return QXRshift(x)

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.Identifier()
        return QXRev(x)

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.Identifier()
        v = self.visitVexp(ctx.vexp())
        return QXQFT(x,v)


    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.Identifier()
        return QXRQFT(x)

    def visit(self, ctx: ParserRuleContext):
        if isinstance(ctx, XMLExpParser.RootContext):
            return self.visitRoot(ctx)
        elif isinstance(ctx, XMLExpParser.ProgramContext):
            return self.visitProgram(ctx)
        elif isinstance(ctx, XMLExpParser.NextexpContext):
            return self.visitNextexp(ctx)
        elif isinstance(ctx, XMLExpParser.ExpContext):
            return self.visitExp(ctx)
        elif isinstance(ctx, XMLExpParser.LetexpContext):
            return self.visitLetexp(ctx)
        elif isinstance(ctx, XMLExpParser.AppexpContext):
            return self.visitAppexp(ctx)
        elif isinstance(ctx, XMLExpParser.IfexpContext):
            return self.visitIfexp(ctx)
        elif isinstance(ctx, XMLExpParser.MatchexpContext):
            return self.visitMatchexp(ctx)
        elif isinstance(ctx, XMLExpParser.ExppairContext):
            return self.visitExppair(ctx)
        elif isinstance(ctx, XMLExpParser.SkipexpContext):
            return self.visitSkipexp(ctx)
        elif isinstance(ctx, XMLExpParser.XexpContext):
            return self.visitXexp(ctx)
        elif isinstance(ctx, XMLExpParser.CuexpContext):
            return self.visitCUexp(ctx)
        elif isinstance(ctx, XMLExpParser.SrexpContext):
            return self.visitSrexp(ctx)
        elif isinstance(ctx, XMLExpParser.LshiftexpContext):
            return self.visitLshiftexp(ctx)
        elif isinstance(ctx, XMLExpParser.RshiftexpContext):
            return self.visitRshiftexp(ctx)
        elif isinstance(ctx, XMLExpParser.RevexpContext):
            return self.visitRevexp(ctx)
        elif isinstance(ctx, XMLExpParser.QftexpContext):
            return self.visitQftexp(ctx)
        elif isinstance(ctx, XMLExpParser.RqftexpContext):
            return self.visitRqftexp(ctx)
        elif isinstance(ctx, XMLExpParser.BlockexpContext):
            return self.visitBlockexp(ctx)
        elif isinstance(ctx, XMLExpParser.ElementContext):
            return self.visitElement(ctx)
        elif isinstance(ctx, XMLExpParser.IdexpContext):
            return self.visitIdexp(ctx)
        elif isinstance(ctx, XMLExpParser.AtypeContext):
            return self.visitAtype(ctx)
        elif isinstance(ctx, XMLExpParser.VexpContext):
            return self.visitVexp(ctx)
        elif isinstance(ctx, XMLExpParser.OpContext):
            return self.visitOp(ctx)
        elif isinstance(ctx, XMLExpParser.NumexpContext):
            return self.visitNumexp(ctx)
        else:
            return super().visit(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        x = ctx.Identifier()
        if ctx.atype() is not None:
            t = self.visitAtype(ctx.atype())
            return QXIDExp(x, t)
        else:
            return QXIDExp(x, None)

    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.idexp() is not None:
            return self.visitIdexp(ctx.idexp())
        if ctx.NUM() is not None:
            v = self.visitNumexp(ctx.numexp())
            return QXNum(v)
        else:
            op = self.visitOp(ctx.op())
            v1 = self.visitVexp(ctx.vexp(0))
            v2 = self.visitVexp(ctx.vexp(1))
            return QXBin(op, v1, v2)
    # the only thing that matters will be 48 and 47

    def visitOp(self, ctx:XMLExpParser.OpContext):
        if ctx.Plus() is not None:
            return "Plus"
        elif ctx.Minus() is not None:
            return "Minus"
        elif ctx.Times() is not None:
            return "Times"
        elif ctx.Div() is not None:
            return "Div"
        elif ctx.Exp() is not None:
            return "Exp"
        elif ctx.GNum() is not None:
            return "GNum"

    def visitAtype(self, ctx:XMLExpParser.AtypeContext):
        if ctx.Nat() is not None:
            return Nat()
        if ctx.Qt() is not None:
            v = self.visitElement(ctx.element(0))
            return Qty(v)
        if ctx.Nor() is not None:
            v = self.visitElement(ctx.element(0))
            return Qty(v, "Nor")
        if ctx.Nor() is not None:
            v = self.visitElement(ctx.element(0))
            v1 = self.visitElement(ctx.element(1))
            return Qty(v, "Phi", v1)

    def visitNumexp(self, ctx:XMLExpParser.NumexpContext):
        return int(ctx.getText())

    #def visitTerminal(self, node):
        # print("terminal")
    #    if node.getSymbol().type == XMLExpParser.Identifier:
    #        return node.getText()
    #    if node.getSymbol().type == XMLExpParser.Number:
    #        return int(node.getText())
    #    print("here1")
    #    return None
