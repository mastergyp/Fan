# Generated from /Users/nelson/PycharmProjects/fan/grammar/src/Fan.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FanParser import FanParser
else:
    from FanParser import FanParser

# This class defines a complete generic visitor for a parse tree produced by FanParser.

class FanVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FanParser#prog.
    def visitProg(self, ctx:FanParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#statements.
    def visitStatements(self, ctx:FanParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#statement.
    def visitStatement(self, ctx:FanParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#terminated.
    def visitTerminated(self, ctx:FanParser.TerminatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#expr.
    def visitExpr(self, ctx:FanParser.ExprContext):
        return self.visitChildren(ctx)



del FanParser