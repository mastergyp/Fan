# Generated from /Users/nelson/PycharmProjects/fan/grammar/src/Fan.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6$\n\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\62\n\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6E\n\6\3\6\3\6\3\6\3\6\5\6K\n\6\3\6\3\6\7")
        buf.write("\6O\n\6\f\6\16\6R\13\6\3\7\3\7\3\7\3\7\7\7X\n\7\f\7\16")
        buf.write("\7[\13\7\3\7\3\7\3\7\5\7`\n\7\3\7\2\3\n\b\2\4\6\b\n\f")
        buf.write("\2\6\3\2\32\33\3\2\34\35\3\2\16\23\3\2\24\25\2n\2\16\3")
        buf.write("\2\2\2\4\24\3\2\2\2\6\27\3\2\2\2\b\31\3\2\2\2\n\61\3\2")
        buf.write("\2\2\f_\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2")
        buf.write("\2\21\23\5\6\4\2\22\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2")
        buf.write("\2\2\24\25\3\2\2\2\25\5\3\2\2\2\26\24\3\2\2\2\27\30\5")
        buf.write("\b\5\2\30\7\3\2\2\2\31\32\5\n\6\2\32\33\7\31\2\2\33\t")
        buf.write("\3\2\2\2\34\35\b\6\1\2\35\36\7\t\2\2\36\37\5\n\6\2\37")
        buf.write(" \7\n\2\2 #\5\n\6\2!\"\7\13\2\2\"$\5\n\6\2#!\3\2\2\2#")
        buf.write("$\3\2\2\2$\62\3\2\2\2%&\7!\2\2&\'\7\37\2\2\'\62\5\n\6")
        buf.write("\17()\7\7\2\2)*\5\n\6\2*+\7\b\2\2+\62\3\2\2\2,\62\7 \2")
        buf.write("\2-\62\7!\2\2.\62\7\6\2\2/\60\7\f\2\2\60\62\5\n\6\3\61")
        buf.write("\34\3\2\2\2\61%\3\2\2\2\61(\3\2\2\2\61,\3\2\2\2\61-\3")
        buf.write("\2\2\2\61.\3\2\2\2\61/\3\2\2\2\62P\3\2\2\2\63\64\f\13")
        buf.write("\2\2\64\65\7\36\2\2\65O\5\n\6\13\66\67\f\n\2\2\678\t\2")
        buf.write("\2\28O\5\n\6\139:\f\t\2\2:;\t\3\2\2;O\5\n\6\n<=\f\b\2")
        buf.write("\2=>\t\4\2\2>O\5\n\6\t?@\f\7\2\2@A\t\5\2\2AO\5\n\6\bB")
        buf.write("D\f\16\2\2CE\7\26\2\2DC\3\2\2\2DE\3\2\2\2EF\3\2\2\2FG")
        buf.write("\7\r\2\2GO\7!\2\2HJ\f\r\2\2IK\7\26\2\2JI\3\2\2\2JK\3\2")
        buf.write("\2\2KL\3\2\2\2LM\7\r\2\2MO\5\f\7\2N\63\3\2\2\2N\66\3\2")
        buf.write("\2\2N9\3\2\2\2N<\3\2\2\2N?\3\2\2\2NB\3\2\2\2NH\3\2\2\2")
        buf.write("OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\13\3\2\2\2RP\3\2\2\2S")
        buf.write("T\7\3\2\2TY\7!\2\2UV\7\4\2\2VX\7!\2\2WU\3\2\2\2X[\3\2")
        buf.write("\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\`\7\5\2")
        buf.write("\2]^\7\3\2\2^`\7\5\2\2_S\3\2\2\2_]\3\2\2\2`\r\3\2\2\2")
        buf.write("\13\24#\61DJNPY_")
        return buf.getvalue()


class FanParser ( Parser ):

    grammarFileName = "Fan.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "<INVALID>", "'('", 
                     "')'", "'if'", "'then'", "'else'", "'print'", "'in'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'and'", 
                     "'or'", "'not'", "'True'", "'False'", "';'", "'/'", 
                     "'*'", "'+'", "'-'", "'^'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "LPAREN", "RPAREN", "IF", "THEN", "ELSE", 
                      "PRINT", "IN", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", 
                      "AND", "OR", "NOT", "TRUE", "FALSE", "TERMINATED", 
                      "DIV", "MUL", "PLUS", "MINUS", "POWER", "ASSIGN", 
                      "NUMBER", "ID", "BLOCK_COMMENT", "LINE_COMMENT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_terminated = 3
    RULE_expr = 4
    RULE_array = 5

    ruleNames =  [ "prog", "statements", "statement", "terminated", "expr", 
                   "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    STRING=4
    LPAREN=5
    RPAREN=6
    IF=7
    THEN=8
    ELSE=9
    PRINT=10
    IN=11
    EQ=12
    NEQ=13
    GT=14
    LT=15
    GTE=16
    LTE=17
    AND=18
    OR=19
    NOT=20
    TRUE=21
    FALSE=22
    TERMINATED=23
    DIV=24
    MUL=25
    PLUS=26
    MINUS=27
    POWER=28
    ASSIGN=29
    NUMBER=30
    ID=31
    BLOCK_COMMENT=32
    LINE_COMMENT=33
    NEWLINE=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(FanParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(FanParser.EOF, 0)

        def getRuleIndex(self):
            return FanParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = FanParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.statements()
            self.state = 13
            self.match(FanParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.StatementContext)
            else:
                return self.getTypedRuleContext(FanParser.StatementContext,i)


        def getRuleIndex(self):
            return FanParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = FanParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FanParser.STRING) | (1 << FanParser.LPAREN) | (1 << FanParser.IF) | (1 << FanParser.PRINT) | (1 << FanParser.NUMBER) | (1 << FanParser.ID))) != 0):
                self.state = 15
                self.statement()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminated(self):
            return self.getTypedRuleContext(FanParser.TerminatedContext,0)


        def getRuleIndex(self):
            return FanParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = FanParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.terminated()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminatedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERMINATED(self):
            return self.getToken(FanParser.TERMINATED, 0)

        def expr(self):
            return self.getTypedRuleContext(FanParser.ExprContext,0)


        def getRuleIndex(self):
            return FanParser.RULE_terminated

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminated" ):
                listener.enterTerminated(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminated" ):
                listener.exitTerminated(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminated" ):
                return visitor.visitTerminated(self)
            else:
                return visitor.visitChildren(self)




    def terminated(self):

        localctx = FanParser.TerminatedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_terminated)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.expr(0)
            self.state = 24
            self.match(FanParser.TERMINATED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FanParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class InListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FanParser.ExprContext,0)

        def IN(self):
            return self.getToken(FanParser.IN, 0)
        def array(self):
            return self.getTypedRuleContext(FanParser.ArrayContext,0)

        def NOT(self):
            return self.getToken(FanParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInList" ):
                listener.enterInList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInList" ):
                listener.exitInList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInList" ):
                return visitor.visitInList(self)
            else:
                return visitor.visitChildren(self)


    class PlusAndMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(FanParser.MINUS, 0)
        def PLUS(self):
            return self.getToken(FanParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusAndMinus" ):
                listener.enterPlusAndMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusAndMinus" ):
                listener.exitPlusAndMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusAndMinus" ):
                return visitor.visitPlusAndMinus(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(FanParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(FanParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(FanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class InFieldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FanParser.ExprContext,0)

        def IN(self):
            return self.getToken(FanParser.IN, 0)
        def ID(self):
            return self.getToken(FanParser.ID, 0)
        def NOT(self):
            return self.getToken(FanParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInField" ):
                listener.enterInField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInField" ):
                listener.exitInField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInField" ):
                return visitor.visitInField(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FanParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class MulAndDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)

        def MUL(self):
            return self.getToken(FanParser.MUL, 0)
        def DIV(self):
            return self.getToken(FanParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulAndDiv" ):
                listener.enterMulAndDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulAndDiv" ):
                listener.exitMulAndDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulAndDiv" ):
                return visitor.visitMulAndDiv(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FanParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(FanParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(FanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FanParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)

        def EQ(self):
            return self.getToken(FanParser.EQ, 0)
        def NEQ(self):
            return self.getToken(FanParser.NEQ, 0)
        def GT(self):
            return self.getToken(FanParser.GT, 0)
        def LT(self):
            return self.getToken(FanParser.LT, 0)
        def GTE(self):
            return self.getToken(FanParser.GTE, 0)
        def LTE(self):
            return self.getToken(FanParser.LTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(FanParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)

        def THEN(self):
            return self.getToken(FanParser.THEN, 0)
        def ELSE(self):
            return self.getToken(FanParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class PowerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)

        def POWER(self):
            return self.getToken(FanParser.POWER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)


    class BooleanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)

        def AND(self):
            return self.getToken(FanParser.AND, 0)
        def OR(self):
            return self.getToken(FanParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpr" ):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(FanParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(FanParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(FanParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FanParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = FanParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 27
                self.match(FanParser.IF)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(FanParser.THEN)
                self.state = 30
                self.expr(0)
                self.state = 33
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 31
                    self.match(FanParser.ELSE)
                    self.state = 32
                    self.expr(0)


                pass

            elif la_ == 2:
                localctx = FanParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(FanParser.ID)
                self.state = 36
                self.match(FanParser.ASSIGN)
                self.state = 37
                self.expr(13)
                pass

            elif la_ == 3:
                localctx = FanParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(FanParser.LPAREN)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(FanParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = FanParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(FanParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = FanParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(FanParser.ID)
                pass

            elif la_ == 6:
                localctx = FanParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(FanParser.STRING)
                pass

            elif la_ == 7:
                localctx = FanParser.PrintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(FanParser.PRINT)
                self.state = 46
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = FanParser.PowerContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")

                        self.state = 50
                        self.match(FanParser.POWER)
                        self.state = 51
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = FanParser.MulAndDivContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==FanParser.DIV or _la==FanParser.MUL):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = FanParser.PlusAndMinusContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not(_la==FanParser.PLUS or _la==FanParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = FanParser.BooleanContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 59
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FanParser.EQ) | (1 << FanParser.NEQ) | (1 << FanParser.GT) | (1 << FanParser.LT) | (1 << FanParser.GTE) | (1 << FanParser.LTE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = FanParser.BooleanExprContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 62
                        _la = self._input.LA(1)
                        if not(_la==FanParser.AND or _la==FanParser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = FanParser.InFieldContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 66
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==FanParser.NOT:
                            self.state = 65
                            self.match(FanParser.NOT)


                        self.state = 68
                        self.match(FanParser.IN)
                        self.state = 69
                        self.match(FanParser.ID)
                        pass

                    elif la_ == 7:
                        localctx = FanParser.InListContext(self, FanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 72
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==FanParser.NOT:
                            self.state = 71
                            self.match(FanParser.NOT)


                        self.state = 74
                        self.match(FanParser.IN)
                        self.state = 75
                        self.array()
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(FanParser.ID)
            else:
                return self.getToken(FanParser.ID, i)

        def getRuleIndex(self):
            return FanParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = FanParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(FanParser.T__0)
                self.state = 82
                self.match(FanParser.ID)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FanParser.T__1:
                    self.state = 83
                    self.match(FanParser.T__1)
                    self.state = 84
                    self.match(FanParser.ID)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(FanParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(FanParser.T__0)
                self.state = 92
                self.match(FanParser.T__2)
                pass


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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         




