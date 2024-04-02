# Generated from SpecExp.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\4\3\4\3\4\5\4\36\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\3\5\3\5\3\5\5\5@\n")
        buf.write("\5\3\5\2\3\6\6\2\4\6\b\2\2\2H\2\n\3\2\2\2\4\16\3\2\2\2")
        buf.write("\6\35\3\2\2\2\b?\3\2\2\2\n\13\5\4\3\2\13\f\7\3\2\2\f\r")
        buf.write("\5\4\3\2\r\3\3\2\2\2\16\17\7\4\2\2\17\20\5\6\4\2\20\27")
        buf.write("\7\f\2\2\21\22\7\4\2\2\22\23\5\6\4\2\23\24\7\f\2\2\24")
        buf.write("\26\3\2\2\2\25\21\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\5\3\2\2\2\31\27\3\2\2\2\32\33\b\4\1")
        buf.write("\2\33\36\7\16\2\2\34\36\5\b\5\2\35\32\3\2\2\2\35\34\3")
        buf.write("\2\2\2\369\3\2\2\2\37 \f\n\2\2 !\7\5\2\2!8\5\6\4\13\"")
        buf.write("#\f\t\2\2#$\7\6\2\2$8\5\6\4\n%&\f\b\2\2&\'\7\7\2\2\'8")
        buf.write("\5\6\4\t()\f\7\2\2)*\7\b\2\2*8\5\6\4\b+,\f\6\2\2,-\7\t")
        buf.write("\2\2-8\5\6\4\7./\f\5\2\2/\60\7\n\2\2\608\5\6\4\6\61\62")
        buf.write("\f\4\2\2\62\63\7\13\2\2\638\5\6\4\5\64\65\f\3\2\2\65\66")
        buf.write("\7\f\2\2\668\5\6\4\4\67\37\3\2\2\2\67\"\3\2\2\2\67%\3")
        buf.write("\2\2\2\67(\3\2\2\2\67+\3\2\2\2\67.\3\2\2\2\67\61\3\2\2")
        buf.write("\2\67\64\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\7\3")
        buf.write("\2\2\2;9\3\2\2\2<@\7\r\2\2=>\7\6\2\2>@\7\r\2\2?<\3\2\2")
        buf.write("\2?=\3\2\2\2@\t\3\2\2\2\7\27\35\679?")
        return buf.getvalue()


class SpecExpParser ( Parser ):

    grammarFileName = "SpecExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'|'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'<'", "'='", "'>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Plus", "Minus", 
                      "Mult", "Div", "Mod", "Less", "Equal", "Greater", 
                      "Number", "Identifier", "Letter", "LetterOrDigit", 
                      "StrLiteral", "AT", "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    RULE_program = 0
    RULE_aexp = 1
    RULE_vexp = 2
    RULE_numexp = 3

    ruleNames =  [ "program", "aexp", "vexp", "numexp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Plus=3
    Minus=4
    Mult=5
    Div=6
    Mod=7
    Less=8
    Equal=9
    Greater=10
    Number=11
    Identifier=12
    Letter=13
    LetterOrDigit=14
    StrLiteral=15
    AT=16
    ELLIPSIS=17
    WS=18
    Comment=19
    Line_Comment=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecExpParser.AexpContext)
            else:
                return self.getTypedRuleContext(SpecExpParser.AexpContext,i)


        def getRuleIndex(self):
            return SpecExpParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SpecExpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.aexp()
            self.state = 9
            self.match(SpecExpParser.T__0)
            self.state = 10
            self.aexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecExpParser.VexpContext)
            else:
                return self.getTypedRuleContext(SpecExpParser.VexpContext,i)


        def Greater(self, i:int=None):
            if i is None:
                return self.getTokens(SpecExpParser.Greater)
            else:
                return self.getToken(SpecExpParser.Greater, i)

        def getRuleIndex(self):
            return SpecExpParser.RULE_aexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexp" ):
                listener.enterAexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexp" ):
                listener.exitAexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexp" ):
                return visitor.visitAexp(self)
            else:
                return visitor.visitChildren(self)




    def aexp(self):

        localctx = SpecExpParser.AexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_aexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(SpecExpParser.T__1)
            self.state = 13
            self.vexp(0)
            self.state = 14
            self.match(SpecExpParser.Greater)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SpecExpParser.T__1:
                self.state = 15
                self.match(SpecExpParser.T__1)
                self.state = 16
                self.vexp(0)
                self.state = 17
                self.match(SpecExpParser.Greater)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SpecExpParser.Identifier, 0)

        def numexp(self):
            return self.getTypedRuleContext(SpecExpParser.NumexpContext,0)


        def vexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecExpParser.VexpContext)
            else:
                return self.getTypedRuleContext(SpecExpParser.VexpContext,i)


        def Plus(self):
            return self.getToken(SpecExpParser.Plus, 0)

        def Minus(self):
            return self.getToken(SpecExpParser.Minus, 0)

        def Mult(self):
            return self.getToken(SpecExpParser.Mult, 0)

        def Div(self):
            return self.getToken(SpecExpParser.Div, 0)

        def Mod(self):
            return self.getToken(SpecExpParser.Mod, 0)

        def Less(self):
            return self.getToken(SpecExpParser.Less, 0)

        def Equal(self):
            return self.getToken(SpecExpParser.Equal, 0)

        def Greater(self):
            return self.getToken(SpecExpParser.Greater, 0)

        def getRuleIndex(self):
            return SpecExpParser.RULE_vexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVexp" ):
                listener.enterVexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVexp" ):
                listener.exitVexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVexp" ):
                return visitor.visitVexp(self)
            else:
                return visitor.visitChildren(self)



    def vexp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecExpParser.VexpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_vexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecExpParser.Identifier]:
                self.state = 25
                self.match(SpecExpParser.Identifier)
                pass
            elif token in [SpecExpParser.Minus, SpecExpParser.Number]:
                self.state = 26
                self.numexp()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 29
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 30
                        self.match(SpecExpParser.Plus)
                        self.state = 31
                        self.vexp(9)
                        pass

                    elif la_ == 2:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 32
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 33
                        self.match(SpecExpParser.Minus)
                        self.state = 34
                        self.vexp(8)
                        pass

                    elif la_ == 3:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 35
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 36
                        self.match(SpecExpParser.Mult)
                        self.state = 37
                        self.vexp(7)
                        pass

                    elif la_ == 4:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        self.match(SpecExpParser.Div)
                        self.state = 40
                        self.vexp(6)
                        pass

                    elif la_ == 5:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        self.match(SpecExpParser.Mod)
                        self.state = 43
                        self.vexp(5)
                        pass

                    elif la_ == 6:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(SpecExpParser.Less)
                        self.state = 46
                        self.vexp(4)
                        pass

                    elif la_ == 7:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 47
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 48
                        self.match(SpecExpParser.Equal)
                        self.state = 49
                        self.vexp(3)
                        pass

                    elif la_ == 8:
                        localctx = SpecExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 50
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 51
                        self.match(SpecExpParser.Greater)
                        self.state = 52
                        self.vexp(2)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NumexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self):
            return self.getToken(SpecExpParser.Number, 0)

        def Minus(self):
            return self.getToken(SpecExpParser.Minus, 0)

        def getRuleIndex(self):
            return SpecExpParser.RULE_numexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumexp" ):
                listener.enterNumexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumexp" ):
                listener.exitNumexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumexp" ):
                return visitor.visitNumexp(self)
            else:
                return visitor.visitChildren(self)




    def numexp(self):

        localctx = SpecExpParser.NumexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numexp)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecExpParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SpecExpParser.Number)
                pass
            elif token in [SpecExpParser.Minus]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(SpecExpParser.Minus)
                self.state = 60
                self.match(SpecExpParser.Number)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.vexp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def vexp_sempred(self, localctx:VexpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




