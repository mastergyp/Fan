# Generated from /Users/nelson/PycharmProjects/fan/grammar/src/Fan.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\'")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\62\n\6\f")
        buf.write("\6\16\6\65\13\6\3\6\2\3\n\7\2\4\6\b\n\2\4\3\2\6\7\3\2")
        buf.write("\b\t\29\2\f\3\2\2\2\4\22\3\2\2\2\6\25\3\2\2\2\b\27\3\2")
        buf.write("\2\2\n&\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2")
        buf.write("\17\21\5\6\4\2\20\17\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\5\3\2\2\2\24\22\3\2\2\2\25\26\5\b")
        buf.write("\5\2\26\7\3\2\2\2\27\30\5\n\6\2\30\31\7\5\2\2\31\t\3\2")
        buf.write("\2\2\32\33\b\6\1\2\33\34\7\r\2\2\34\35\7\13\2\2\35\'\5")
        buf.write("\n\6\n\36\37\7\3\2\2\37 \5\n\6\2 !\7\4\2\2!\'\3\2\2\2")
        buf.write("\"#\7\t\2\2#\'\5\n\6\7$\'\7\f\2\2%\'\7\r\2\2&\32\3\2\2")
        buf.write("\2&\36\3\2\2\2&\"\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'\63\3\2")
        buf.write("\2\2()\f\b\2\2)*\7\n\2\2*\62\5\n\6\t+,\f\6\2\2,-\t\2\2")
        buf.write("\2-\62\5\n\6\7./\f\5\2\2/\60\t\3\2\2\60\62\5\n\6\6\61")
        buf.write("(\3\2\2\2\61+\3\2\2\2\61.\3\2\2\2\62\65\3\2\2\2\63\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\13\3\2\2\2\65\63\3\2\2\2\6\22")
        buf.write("&\61\63")
        return buf.getvalue()


class FanParser ( Parser ):

    grammarFileName = "Fan.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'/'", "'*'", "'+'", 
                     "'-'", "'^'", "'='" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "TERMINATED", "DIV", 
                      "MUL", "PLUS", "MINUS", "POWER", "ASSIGN", "INT", 
                      "ID", "BLOCK_COMMENT", "LINE_COMMENT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_terminated = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "statements", "statement", "terminated", "expr" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    TERMINATED=3
    DIV=4
    MUL=5
    PLUS=6
    MINUS=7
    POWER=8
    ASSIGN=9
    INT=10
    ID=11
    BLOCK_COMMENT=12
    LINE_COMMENT=13
    NEWLINE=14
    WS=15

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
            self.state = 10
            self.statements()
            self.state = 11
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
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FanParser.LPAREN) | (1 << FanParser.MINUS) | (1 << FanParser.INT) | (1 << FanParser.ID))) != 0):
                self.state = 13
                self.statement()
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
            self.state = 19
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
            self.state = 21
            self.expr(0)
            self.state = 22
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

        def ID(self):
            return self.getToken(FanParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(FanParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FanParser.ExprContext)
            else:
                return self.getTypedRuleContext(FanParser.ExprContext,i)


        def LPAREN(self):
            return self.getToken(FanParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(FanParser.RPAREN, 0)

        def MINUS(self):
            return self.getToken(FanParser.MINUS, 0)

        def INT(self):
            return self.getToken(FanParser.INT, 0)

        def POWER(self):
            return self.getToken(FanParser.POWER, 0)

        def MUL(self):
            return self.getToken(FanParser.MUL, 0)

        def DIV(self):
            return self.getToken(FanParser.DIV, 0)

        def PLUS(self):
            return self.getToken(FanParser.PLUS, 0)

        def getRuleIndex(self):
            return FanParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
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
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 25
                self.match(FanParser.ID)
                self.state = 26
                self.match(FanParser.ASSIGN)
                self.state = 27
                self.expr(8)
                pass

            elif la_ == 2:
                self.state = 28
                self.match(FanParser.LPAREN)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(FanParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 32
                self.match(FanParser.MINUS)
                self.state = 33
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 34
                self.match(FanParser.INT)
                pass

            elif la_ == 5:
                self.state = 35
                self.match(FanParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = FanParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 39
                        self.match(FanParser.POWER)
                        self.state = 40
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = FanParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==FanParser.DIV or _la==FanParser.MUL):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = FanParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        _la = self._input.LA(1)
                        if not(_la==FanParser.PLUS or _la==FanParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(4)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




