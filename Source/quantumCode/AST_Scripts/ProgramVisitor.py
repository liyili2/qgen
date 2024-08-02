from Source.quantumCode.AST_Scripts.XMLProgrammer import *


class ProgramVisitor:

    # Visit a parse tree produced by XMLExpParser#root.
    def visitRoot(self, ctx: XMLProgramer.QXRoot):
        return ctx.program().accept(self)

    # Visit a parse tree produced by XMLExpParser#nextexp.
    def visitNext(self, ctx: XMLProgramer.QXNext):
        return ctx.program().accept(self)

    # Visit a parse tree produced by XMLExpParser#program.
    def visitProgram(self, ctx: XMLProgramer.QXProgram):
        i = 0
        while ctx.exp(i) is not None:
            ctx.exp(i).accept(self)
            i = i + 1

    # Visit a parse tree produced by XMLExpParser#exp.

    # Visit a parse tree produced by XMLExpParser#blockexp.
    def visitBlock(self, ctx: XMLProgramer.QXBlock):
        pass

    def visitLet(self, ctx: XMLProgramer.QXLet):
        return ctx.program().accept(self)

    def visitApp(self, ctx: XMLProgramer.QXApp):
        i = 0
        while ctx.vexp(i) is not None:
            ctx.vexp(i).accept(self)

    def visitCU(self, ctx: XMLProgramer.QXCU):
        return ctx.program().accept(self)

    def visitIf(self, ctx: XMLProgramer.QXIf):
        ctx.vexp().accept(self)
        ctx.left().accept(self)
        ctx.right().accept(self)

    def visitMatch(self, ctx: XMLProgramer.QXMatch):
        ctx.zero().accept(self)
        ctx.multi().accept(self)

    def visitPair(self, ctx: XMLProgramer.QXPair):
        ctx.elem().accept(self)
        ctx.program().accept(self)

    def visitBin(self, ctx: XMLProgramer.QXBin):
        ctx.left().accept(self)
        ctx.right().accept(self)

    def visitIDExp(self, ctx: XMLProgramer.QXIDExp):
        ctx.type().accept(self)

    def visitNum(self, ctx: XMLProgramer.QXNum):
        pass

    def visitQTy(self, ctx: XMLProgramer.Qty):
        ctx.get_num().accept(self)

    def visitNat(self, ctx: XMLProgramer.Nat):
        pass

    def visitFun(self, ctx: XMLProgramer.Fun):
        pass

    def visitSKIP(self, ctx: XMLProgramer.QXSKIP):
        ctx.vexp().accept(self)

    def visitX(self, ctx: XMLProgramer.QXX):
        ctx.vexp().accept(self)

    def visitSR(self, ctx: XMLProgramer.QXSR):
        ctx.vexp().accept(self)

    def visitQFT(self, ctx: XMLProgramer.QXQFT):
        ctx.vexp().accept(self)

    def visitRQFT(self, ctx: XMLProgramer.QXRQFT):
        pass

    def visitLshift(self, ctx: XMLProgramer.QXLshift):
        pass

    def visitRshift(self, ctx: XMLProgramer.QXRshift):
        pass

    def visitRev(self, ctx: XMLProgramer.QXRev):
        pass
