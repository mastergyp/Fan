# Generated from /Users/yufan/shared/repos/Fan/grammar/src/Fan.g4 by ANTLR 4.7.2
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


    # Visit a parse tree produced by FanParser#Return.
    def visitReturn(self, ctx:FanParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#InList.
    def visitInList(self, ctx:FanParser.InListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#PlusAndMinus.
    def visitPlusAndMinus(self, ctx:FanParser.PlusAndMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#String.
    def visitString(self, ctx:FanParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Print.
    def visitPrint(self, ctx:FanParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#InField.
    def visitInField(self, ctx:FanParser.InFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Number.
    def visitNumber(self, ctx:FanParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#MulAndDiv.
    def visitMulAndDiv(self, ctx:FanParser.MulAndDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Assign.
    def visitAssign(self, ctx:FanParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#FunctionCall.
    def visitFunctionCall(self, ctx:FanParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Id.
    def visitId(self, ctx:FanParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Boolean.
    def visitBoolean(self, ctx:FanParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#If.
    def visitIf(self, ctx:FanParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Power.
    def visitPower(self, ctx:FanParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#BooleanExpr.
    def visitBooleanExpr(self, ctx:FanParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#Paren.
    def visitParen(self, ctx:FanParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FanParser#array.
    def visitArray(self, ctx:FanParser.ArrayContext):
        return self.visitChildren(ctx)



del FanParser