from quantumCode.AST_Scripts import XMLProgrammer

from Source.quantumCode.AST_Scripts.AbstractProgramVisitor import AbstractProgramVisitor


class ProgramVisitor(AbstractProgramVisitor):

    # Visit a parse tree produced by XMLExpParser#root.
    def visitRoot(self, ctx: XMLProgrammer.QXRoot):
        return ctx.program().accept(self)

    # Visit a parse tree produced by XMLExpParser#nextexp.
    def visitNext(self, ctx: XMLProgrammer.QXNext):
        return ctx.program().accept(self)

    # Visit a parse tree produced by XMLExpParser#program.
    def visitProgram(self, ctx: XMLProgrammer.QXProgram):
        i = 0
        while ctx.exp(i) is not None:
            ctx.exp(i).accept(self)
            i = i + 1

    # Visit a parse tree produced by XMLExpParser#exp.

    # Visit a parse tree produced by XMLExpParser#blockexp.
    def visitBlock(self, ctx: XMLProgrammer.QXBlock):
        pass

    def visitLet(self, ctx: XMLProgrammer.QXLet):
        return ctx.program().accept(self)

    def visitApp(self, ctx: XMLProgrammer.QXApp):
        i = 0
        while ctx.vexp(i) is not None:
            ctx.vexp(i).accept(self)

    def visitCU(self, ctx: XMLProgrammer.QXCU):
        return ctx.program().accept(self)

    def visitIf(self, ctx: XMLProgrammer.QXIf):
        ctx.vexp().accept(self)
        ctx.left().accept(self)
        ctx.right().accept(self)

    def visitMatch(self, ctx: XMLProgrammer.QXMatch):
        ctx.zero().accept(self)
        ctx.multi().accept(self)

    def visitPair(self, ctx: XMLProgrammer.QXPair):
        ctx.elem().accept(self)
        ctx.program().accept(self)

    def visitBin(self, ctx: XMLProgrammer.QXBin):
        ctx.left().accept(self)
        ctx.right().accept(self)

    def visitIDExp(self, ctx: XMLProgrammer.QXIDExp):
        ctx.type().accept(self)

    def visitNum(self, ctx: XMLProgrammer.QXNum):
        pass

    def visitQTy(self, ctx: XMLProgrammer.Qty):
        ctx.get_num().accept(self)

    def visitNat(self, ctx: XMLProgrammer.Nat):
        pass

    def visitFun(self, ctx: XMLProgrammer.Fun):
        pass

    def visitSKIP(self, ctx: XMLProgrammer.QXSKIP):
        ctx.vexp().accept(self)

    def visitX(self, ctx: XMLProgrammer.QXX):
        ctx.vexp().accept(self)

    def visitSR(self, ctx: XMLProgrammer.QXSR):
        ctx.vexp().accept(self)

    def visitQFT(self, ctx: XMLProgrammer.QXQFT):
        ctx.vexp().accept(self)

    def visitRQFT(self, ctx: XMLProgrammer.QXRQFT):
        pass

    def visitLshift(self, ctx: XMLProgrammer.QXLshift):
        pass

    def visitRshift(self, ctx: XMLProgrammer.QXRshift):
        pass

    def visitRev(self, ctx: XMLProgrammer.QXRev):
        pass

