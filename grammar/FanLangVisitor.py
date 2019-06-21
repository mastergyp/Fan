#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 11:06 AM
# @Author  : likaifuismyson@gmail.com
# @Site    : 
# @File    : FanLangVisitor.py
from grammar.build.FanParser import FanParser
from grammar.build.FanVisitor import FanVisitor as FanVisitorOriginal


class FanLangVisitor(FanVisitorOriginal):

    def __init__(self, args_map=None):
        self.args_map = args_map or {}
        self.return_val = None

    def visitInList(self, ctx: FanParser.InListContext):
        return super().visitInList(ctx)

    def visitString(self, ctx: FanParser.StringContext):
        return str(ctx.getText()[1: -1])

    def visitInField(self, ctx: FanParser.InFieldContext):
        return super().visitInField(ctx)

    def visitNumber(self, ctx: FanParser.NumberContext):
        if "." not in ctx.NUMBER().getText():
            return int(ctx.NUMBER().getText())
        else:
            return float(ctx.NUMBER().getText())

    def visitBoolean(self, ctx: FanParser.BooleanContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        boolOpt = ctx.getChild(1).getText()

        if boolOpt == "==":
            if isinstance(left, float) or isinstance(right, float):
                return abs(left - right) < 0.000001

            return left == right
        elif boolOpt == ">":
            if isinstance(left, float) or isinstance(right, float):
                return left - right > 0.000001
            return left > right
        elif boolOpt == ">=":
            return left >= right
        elif boolOpt == "<":
            if isinstance(left, float) or isinstance(right, float):
                return right - left > 0.000001
            return left < right
        elif boolOpt == "<=":
            return left <= right
        elif boolOpt == "!=":
            if isinstance(left, float) or isinstance(right, float):
                return abs(left - right) > 0.000001
            return left != right

    def visitIf(self, ctx: FanParser.IfContext):
        judge = self.visit(ctx.expr(0))

        if judge:
            return self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(2))

    def visitBooleanExpr(self, ctx: FanParser.BooleanExprContext):
        return super().visitBooleanExpr(ctx)

    def visitArray(self, ctx: FanParser.ArrayContext):
        return super().visitArray(ctx)

    def visitProg(self, ctx: FanParser.ProgContext):
        return super().visitProg(ctx)

    def visitStatements(self, ctx: FanParser.StatementsContext):
        return super().visitStatements(ctx)

    def visitTerminated(self, ctx: FanParser.TerminatedContext):
        result = self.visit(ctx.expr())
        return result

    def visitStatement(self, ctx: FanParser.StatementContext):
        return super().visitChildren(ctx)

    def visitMulAndDiv(self, ctx: FanParser.MulAndDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == "*":
            return left * right
        return left / right

    def visitPlusAndMinus(self, ctx: FanParser.PlusAndMinusContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == "+":
            if isinstance(left, str):
                return left + str(right)
            elif isinstance(right, str):
                return str(left) + right
            return left + right
        return left - right

    def visitAssign(self, ctx: FanParser.AssignContext):
        value = self.visit(ctx.expr())
        self.args_map[ctx.ID().getText()] = value
        return value

    def visitId(self, ctx: FanParser.IdContext):
        return self.args_map.get(ctx.ID().getText(), None)

    def visitPower(self, ctx: FanParser.PowerContext):
        return self.visit(ctx.expr(0)) ** self.visit(ctx.expr(1))

    def visitParen(self, ctx: FanParser.ParenContext):
        return self.visit(ctx.expr())

    def visitPrint(self, ctx: FanParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
        return None

    def visitReturn(self, ctx: FanParser.ReturnContext):
        self.return_val = self.visit(ctx.expr())
        return self.return_val
