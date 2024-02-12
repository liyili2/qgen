from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from XMLExpParser import *
import XMLExpVisitor

class Simulator(XMLExpVisitor):
    # Visit a parse tree produced by ExpParser#vexp.
    def visitVexp(self, ctx: ExpParser.VexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#bexp.
    def visitBexp(self, ctx: ExpParser.BexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#posi.
    def visitPosi(self, ctx: ExpParser.PosiContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#exp.
    def visitExp(self, ctx: ExpParser.ExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#skipexp.
    def visitSkipexp(self, ctx: ExpParser.SkipexpContext, st: int):
        return st

    # Visit a parse tree produced by ExpParser#posiexp.
    def visitPosiexp(self, ctx: ExpParser.PosiexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#xgexp.
    def visitXgexp(self, ctx: ExpParser.XgexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#cuexp.
    def visitCuexp(self, ctx: ExpParser.CuexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#rzexp.
    def visitRzexp(self, ctx: ExpParser.RzexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#srexp.
    def visitSrexp(self, ctx: ExpParser.SrexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#lshiftexp.
    def visitLshiftexp(self, ctx: ExpParser.LshiftexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#rshiftexp.
    def visitRshiftexp(self, ctx: ExpParser.RshiftexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#revexp.
    def visitRevexp(self, ctx: ExpParser.RevexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#qftexp.
    def visitQftexp(self, ctx: ExpParser.QftexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#rqftexp.
    def visitRqftexp(self, ctx: ExpParser.RqftexpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpParser#seqexp.
    def visitSeqexp(self, ctx: ExpParser.SeqexpContext):
        return self.visitChildren(ctx)
