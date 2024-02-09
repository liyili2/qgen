# Generated from XMLExp.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\"\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\7\4\66\n\4\f\4\16\49\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5B\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("N\n\6\3\7\3\7\3\7\2\3\6\b\2\4\6\b\n\f\2\3\3\2\16\17\2")
        buf.write("Z\2\16\3\2\2\2\4\25\3\2\2\2\6!\3\2\2\2\bA\3\2\2\2\nM\3")
        buf.write("\2\2\2\fO\3\2\2\2\16\22\5\4\3\2\17\21\5\4\3\2\20\17\3")
        buf.write("\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\3")
        buf.write("\3\2\2\2\24\22\3\2\2\2\25\26\7\3\2\2\26\27\7\24\2\2\27")
        buf.write("\30\7\4\2\2\30\31\5\b\5\2\31\32\7\5\2\2\32\33\7\24\2\2")
        buf.write("\33\34\7\4\2\2\34\5\3\2\2\2\35\36\b\4\1\2\36\"\7\24\2")
        buf.write("\2\37\"\5\n\6\2 \"\5\f\7\2!\35\3\2\2\2!\37\3\2\2\2! \3")
        buf.write("\2\2\2\"\67\3\2\2\2#$\f\b\2\2$%\7\6\2\2%\66\5\6\4\t&\'")
        buf.write("\f\7\2\2\'(\7\7\2\2(\66\5\6\4\b)*\f\6\2\2*+\7\b\2\2+\66")
        buf.write("\5\6\4\7,-\f\5\2\2-.\7\t\2\2.\66\5\6\4\6/\60\f\4\2\2\60")
        buf.write("\61\7\n\2\2\61\66\5\6\4\5\62\63\f\3\2\2\63\64\7\13\2\2")
        buf.write("\64\66\5\6\4\4\65#\3\2\2\2\65&\3\2\2\2\65)\3\2\2\2\65")
        buf.write(",\3\2\2\2\65/\3\2\2\2\65\62\3\2\2\2\669\3\2\2\2\67\65")
        buf.write("\3\2\2\2\678\3\2\2\28\7\3\2\2\29\67\3\2\2\2:B\5\2\2\2")
        buf.write(";B\5\6\4\2<B\7\21\2\2=>\7\22\2\2>?\7\f\2\2?@\7\23\2\2")
        buf.write("@B\7\r\2\2A:\3\2\2\2A;\3\2\2\2A<\3\2\2\2A=\3\2\2\2B\t")
        buf.write("\3\2\2\2CN\7\23\2\2DE\7\7\2\2EN\7\23\2\2FG\7\23\2\2GH")
        buf.write("\7\20\2\2HN\7\23\2\2IJ\7\7\2\2JK\7\23\2\2KL\7\20\2\2L")
        buf.write("N\7\23\2\2MC\3\2\2\2MD\3\2\2\2MF\3\2\2\2MI\3\2\2\2N\13")
        buf.write("\3\2\2\2OP\t\2\2\2P\r\3\2\2\2\b\22!\65\67AM")
        return buf.getvalue()


class XMLExpParser ( Parser ):

    grammarFileName = "XMLExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'</'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'^'", "'('", "')'", "'#t'", "'#f'", 
                     "'.'", "'Nor'", "'QFT'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TrueLiteral", "FalseLiteral", "Dot", "Nor", "QFT", 
                      "Number", "Identifier", "Letter", "LetterOrDigit", 
                      "StrLiteral", "AT", "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    RULE_program = 0
    RULE_xexp = 1
    RULE_vexp = 2
    RULE_nextlevel = 3
    RULE_numexp = 4
    RULE_boolexp = 5

    ruleNames =  [ "program", "xexp", "vexp", "nextlevel", "numexp", "boolexp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    TrueLiteral=12
    FalseLiteral=13
    Dot=14
    Nor=15
    QFT=16
    Number=17
    Identifier=18
    Letter=19
    LetterOrDigit=20
    StrLiteral=21
    AT=22
    ELLIPSIS=23
    WS=24
    Comment=25
    Line_Comment=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLExpParser.XexpContext)
            else:
                return self.getTypedRuleContext(XMLExpParser.XexpContext,i)


        def getRuleIndex(self):
            return XMLExpParser.RULE_program

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

        localctx = XMLExpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.xexp()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XMLExpParser.T__0:
                self.state = 13
                self.xexp()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class XexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(XMLExpParser.Identifier)
            else:
                return self.getToken(XMLExpParser.Identifier, i)

        def nextlevel(self):
            return self.getTypedRuleContext(XMLExpParser.NextlevelContext,0)


        def getRuleIndex(self):
            return XMLExpParser.RULE_xexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXexp" ):
                listener.enterXexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXexp" ):
                listener.exitXexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXexp" ):
                return visitor.visitXexp(self)
            else:
                return visitor.visitChildren(self)




    def xexp(self):

        localctx = XMLExpParser.XexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_xexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(XMLExpParser.T__0)
            self.state = 20
            self.match(XMLExpParser.Identifier)
            self.state = 21
            self.match(XMLExpParser.T__1)
            self.state = 22
            self.nextlevel()
            self.state = 23
            self.match(XMLExpParser.T__2)
            self.state = 24
            self.match(XMLExpParser.Identifier)
            self.state = 25
            self.match(XMLExpParser.T__1)
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
            return self.getToken(XMLExpParser.Identifier, 0)

        def numexp(self):
            return self.getTypedRuleContext(XMLExpParser.NumexpContext,0)


        def boolexp(self):
            return self.getTypedRuleContext(XMLExpParser.BoolexpContext,0)


        def vexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLExpParser.VexpContext)
            else:
                return self.getTypedRuleContext(XMLExpParser.VexpContext,i)


        def getRuleIndex(self):
            return XMLExpParser.RULE_vexp

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
        localctx = XMLExpParser.VexpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_vexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XMLExpParser.Identifier]:
                self.state = 28
                self.match(XMLExpParser.Identifier)
                pass
            elif token in [XMLExpParser.T__4, XMLExpParser.Number]:
                self.state = 29
                self.numexp()
                pass
            elif token in [XMLExpParser.TrueLiteral, XMLExpParser.FalseLiteral]:
                self.state = 30
                self.boolexp()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = XMLExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 33
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 34
                        self.match(XMLExpParser.T__3)
                        self.state = 35
                        self.vexp(7)
                        pass

                    elif la_ == 2:
                        localctx = XMLExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 36
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 37
                        self.match(XMLExpParser.T__4)
                        self.state = 38
                        self.vexp(6)
                        pass

                    elif la_ == 3:
                        localctx = XMLExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(XMLExpParser.T__5)
                        self.state = 41
                        self.vexp(5)
                        pass

                    elif la_ == 4:
                        localctx = XMLExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        self.match(XMLExpParser.T__6)
                        self.state = 44
                        self.vexp(4)
                        pass

                    elif la_ == 5:
                        localctx = XMLExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        self.match(XMLExpParser.T__7)
                        self.state = 47
                        self.vexp(3)
                        pass

                    elif la_ == 6:
                        localctx = XMLExpParser.VexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vexp)
                        self.state = 48
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 49
                        self.match(XMLExpParser.T__8)
                        self.state = 50
                        self.vexp(2)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NextlevelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(XMLExpParser.ProgramContext,0)


        def vexp(self):
            return self.getTypedRuleContext(XMLExpParser.VexpContext,0)


        def Nor(self):
            return self.getToken(XMLExpParser.Nor, 0)

        def QFT(self):
            return self.getToken(XMLExpParser.QFT, 0)

        def Number(self):
            return self.getToken(XMLExpParser.Number, 0)

        def getRuleIndex(self):
            return XMLExpParser.RULE_nextlevel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNextlevel" ):
                listener.enterNextlevel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNextlevel" ):
                listener.exitNextlevel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextlevel" ):
                return visitor.visitNextlevel(self)
            else:
                return visitor.visitChildren(self)




    def nextlevel(self):

        localctx = XMLExpParser.NextlevelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nextlevel)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XMLExpParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.program()
                pass
            elif token in [XMLExpParser.T__4, XMLExpParser.TrueLiteral, XMLExpParser.FalseLiteral, XMLExpParser.Number, XMLExpParser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.vexp(0)
                pass
            elif token in [XMLExpParser.Nor]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(XMLExpParser.Nor)
                pass
            elif token in [XMLExpParser.QFT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.match(XMLExpParser.QFT)
                self.state = 60
                self.match(XMLExpParser.T__9)
                self.state = 61
                self.match(XMLExpParser.Number)
                self.state = 62
                self.match(XMLExpParser.T__10)
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

    class NumexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(XMLExpParser.Number)
            else:
                return self.getToken(XMLExpParser.Number, i)

        def Dot(self):
            return self.getToken(XMLExpParser.Dot, 0)

        def getRuleIndex(self):
            return XMLExpParser.RULE_numexp

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

        localctx = XMLExpParser.NumexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_numexp)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(XMLExpParser.Number)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(XMLExpParser.T__4)
                self.state = 67
                self.match(XMLExpParser.Number)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(XMLExpParser.Number)
                self.state = 69
                self.match(XMLExpParser.Dot)
                self.state = 70
                self.match(XMLExpParser.Number)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(XMLExpParser.T__4)
                self.state = 72
                self.match(XMLExpParser.Number)
                self.state = 73
                self.match(XMLExpParser.Dot)
                self.state = 74
                self.match(XMLExpParser.Number)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TrueLiteral(self):
            return self.getToken(XMLExpParser.TrueLiteral, 0)

        def FalseLiteral(self):
            return self.getToken(XMLExpParser.FalseLiteral, 0)

        def getRuleIndex(self):
            return XMLExpParser.RULE_boolexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolexp" ):
                listener.enterBoolexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolexp" ):
                listener.exitBoolexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexp" ):
                return visitor.visitBoolexp(self)
            else:
                return visitor.visitChildren(self)




    def boolexp(self):

        localctx = XMLExpParser.BoolexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_boolexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not(_la==XMLExpParser.TrueLiteral or _la==XMLExpParser.FalseLiteral):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




