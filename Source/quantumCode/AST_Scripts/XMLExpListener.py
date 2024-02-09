# Generated from XMLExp.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLExpParser import XMLExpParser
else:
    from XMLExpParser import XMLExpParser

# This class defines a complete listener for a parse tree produced by XMLExpParser.
class XMLExpListener(ParseTreeListener):

    # Enter a parse tree produced by XMLExpParser#program.
    def enterProgram(self, ctx:XMLExpParser.ProgramContext):
        pass

    # Exit a parse tree produced by XMLExpParser#program.
    def exitProgram(self, ctx:XMLExpParser.ProgramContext):
        pass


    # Enter a parse tree produced by XMLExpParser#xexp.
    def enterXexp(self, ctx:XMLExpParser.XexpContext):
        pass

    # Exit a parse tree produced by XMLExpParser#xexp.
    def exitXexp(self, ctx:XMLExpParser.XexpContext):
        pass


    # Enter a parse tree produced by XMLExpParser#vexp.
    def enterVexp(self, ctx:XMLExpParser.VexpContext):
        pass

    # Exit a parse tree produced by XMLExpParser#vexp.
    def exitVexp(self, ctx:XMLExpParser.VexpContext):
        pass


    # Enter a parse tree produced by XMLExpParser#nextlevel.
    def enterNextlevel(self, ctx:XMLExpParser.NextlevelContext):
        pass

    # Exit a parse tree produced by XMLExpParser#nextlevel.
    def exitNextlevel(self, ctx:XMLExpParser.NextlevelContext):
        pass


    # Enter a parse tree produced by XMLExpParser#numexp.
    def enterNumexp(self, ctx:XMLExpParser.NumexpContext):
        pass

    # Exit a parse tree produced by XMLExpParser#numexp.
    def exitNumexp(self, ctx:XMLExpParser.NumexpContext):
        pass


    # Enter a parse tree produced by XMLExpParser#typeexp.
    def enterTypeexp(self, ctx:XMLExpParser.TypeexpContext):
        pass

    # Exit a parse tree produced by XMLExpParser#typeexp.
    def exitTypeexp(self, ctx:XMLExpParser.TypeexpContext):
        pass


    # Enter a parse tree produced by XMLExpParser#boolexp.
    def enterBoolexp(self, ctx:XMLExpParser.BoolexpContext):
        pass

    # Exit a parse tree produced by XMLExpParser#boolexp.
    def exitBoolexp(self, ctx:XMLExpParser.BoolexpContext):
        pass


