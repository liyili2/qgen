# Generated from SpecExp.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpecExpParser import SpecExpParser
else:
    from SpecExpParser import SpecExpParser

# This class defines a complete generic visitor for a parse tree produced by SpecExpParser.

class SpecExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpecExpParser#program.
    def visitProgram(self, ctx:SpecExpParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecExpParser#aexp.
    def visitAexp(self, ctx:SpecExpParser.AexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecExpParser#vexp.
    def visitVexp(self, ctx:SpecExpParser.VexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecExpParser#numexp.
    def visitNumexp(self, ctx:SpecExpParser.NumexpContext):
        return self.visitChildren(ctx)



del SpecExpParser