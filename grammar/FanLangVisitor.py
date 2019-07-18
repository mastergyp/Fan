#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 11:06 AM
# @Author  : likaifuismyson@gmail.com
# @Site    : 
# @File    : FanLangVisitor.py
from grammar.build.FanParser import FanParser
from grammar.build.FanVisitor import FanVisitor as FanVisitorOriginal
import logging
logging.basicConfig(level=logging.DEBUG)
from grammar.funcs import func_dict

class FanLangVisitor(FanVisitorOriginal):

    def __init__(self, args_map=None):
        """
        visitor init
        :param args_map: store referenced db info
        """
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

    # Visit a parse tree produced by FanParser#FunctionCall.
    def visitFunctionCall(self, ctx:FanParser.FunctionCallContext):
        args = [item.getText() for i, item in enumerate(ctx.getChildren()) if i % 2 == 0]
        func_name = args.pop(0)
        func_dict[func_name](*args)
        return self.visitChildren(ctx)

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
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == "and":
            return left and right
        elif ctx.getChild(1).getText() == "or":
            return left or right

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
        """
        TODO: 获取字段内容
        :param ctx:
        :return:
        """
        id_name = ctx.ID().getText()
        if id_name not in self.args_map:
            logging.warning("Warning ID: `%s` NOT Defined" % id_name)
            return None
        return self.args_map[id_name]

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

    def visitTrueFalse(self, ctx: FanParser.TrueFalseContext):
        if ctx.getChild(0).getText() == "True":
            return True
        else:
            return False
