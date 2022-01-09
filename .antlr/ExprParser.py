# Generated from c:\Users\Admin\Documents\code practice\Code PPL 212\programing code\learn\test lexer\Expr.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\5\5\37\n\5\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\3\3\2\4\5\2%\2\f\3\2\2\2\4\27\3\2\2")
        buf.write("\2\6\31\3\2\2\2\b\36\3\2\2\2\n \3\2\2\2\f\r\5\4\3\2\r")
        buf.write("\16\7\3\2\2\16\17\7\b\2\2\17\20\7\t\2\2\20\22\7\n\2\2")
        buf.write("\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\25\7\13\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\t\2")
        buf.write("\2\2\30\5\3\2\2\2\31\32\5\n\6\2\32\33\7\f\2\2\33\7\3\2")
        buf.write("\2\2\34\37\5\n\6\2\35\37\7\7\2\2\36\34\3\2\2\2\36\35\3")
        buf.write("\2\2\2\37\t\3\2\2\2 !\7\6\2\2!#\7\b\2\2\"$\5\b\5\2#\"")
        buf.write("\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\t\2\2&\13\3\2\2\2\5\22")
        buf.write("\36#")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "ID", 
                      "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    ID=4
    INTLIT=5
    LB=6
    RB=7
    LP=8
    RP=9
    SEMI=10
    WS=11
    ERROR_CHAR=12
    UNCLOSE_STRING=13
    ILLEGAL_ESCAPE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(ExprParser.MptypeContext,0)


        def LB(self):
            return self.getToken(ExprParser.LB, 0)

        def RB(self):
            return self.getToken(ExprParser.RB, 0)

        def LP(self):
            return self.getToken(ExprParser.LP, 0)

        def RP(self):
            return self.getToken(ExprParser.RP, 0)

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(ExprParser.BodyContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_program




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mptype()
            self.state = 11
            self.match(ExprParser.T__0)
            self.state = 12
            self.match(ExprParser.LB)
            self.state = 13
            self.match(ExprParser.RB)
            self.state = 14
            self.match(ExprParser.LP)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExprParser.ID:
                self.state = 15
                self.body()


            self.state = 18
            self.match(ExprParser.RP)
            self.state = 19
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(ExprParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(ExprParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_mptype




    def mptype(self):

        localctx = ExprParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==ExprParser.INTTYPE or _la==ExprParser.VOIDTYPE):
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


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(ExprParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_body




    def body(self):

        localctx = ExprParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.funcall()
            self.state = 24
            self.match(ExprParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(ExprParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(ExprParser.INTLIT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_exp




    def exp(self):

        localctx = ExprParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.funcall()
                pass
            elif token in [ExprParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(ExprParser.INTLIT)
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


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LB(self):
            return self.getToken(ExprParser.LB, 0)

        def RB(self):
            return self.getToken(ExprParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcall




    def funcall(self):

        localctx = ExprParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ExprParser.ID)
            self.state = 31
            self.match(ExprParser.LB)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExprParser.ID or _la==ExprParser.INTLIT:
                self.state = 32
                self.exp()


            self.state = 35
            self.match(ExprParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





