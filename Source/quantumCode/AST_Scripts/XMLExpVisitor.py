# Generated from XMLExp.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLExpParser import XMLExpParser
else:
    from XMLExpParser import XMLExpParser

# This class defines a complete generic visitor for a parse tree produced by XMLExpParser.

class XMLExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XMLExpParser#program.
    def visitProgram(self, ctx:XMLExpParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLExpParser#xexp.
    def visitXexp(self, ctx:XMLExpParser.XexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx:XMLExpParser.VexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLExpParser#nextlevel.
    def visitNextlevel(self, ctx:XMLExpParser.NextlevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLExpParser#numexp.
    def visitNumexp(self, ctx:XMLExpParser.NumexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLExpParser#boolexp.
    def visitBoolexp(self, ctx:XMLExpParser.BoolexpContext):
        return self.visitChildren(ctx)



del XMLExpParser