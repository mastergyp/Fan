#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 11:06 AM
# @Author  : likaifuismyson@gmail.com
# @Site    : 
# @File    : FanLangVisitor.py
from grammar.build.FanParser import FanParser
from grammar.build.FanVisitor import FanVisitor as FanVisitorOriginal


class FanLangVisitor(FanVisitorOriginal):

    args_map = {}

    def visitProg(self, ctx: FanParser.ProgContext):
        return super().visitProg(ctx)

    def visitStatements(self, ctx: FanParser.StatementsContext):
        return super().visitStatements(ctx)

    def visitTerminated(self, ctx: FanParser.TerminatedContext):
        if ctx.expr():
            result = self.visitExpr(ctx.expr())
            print("the result is " + str(result))
        else:
            result = super().visitTerminated(ctx)
        return result

    def visitStatement(self, ctx: FanParser.StatementContext):
        return super().visitChildren(ctx)

    def visitExpr(self, ctx: FanParser.ExprContext):

        if ctx.INT():
            return int(ctx.INT().getText())

        if ctx.ASSIGN():
            value = self.visit(ctx.expr(0))
            self.args_map[ctx.ID().getText()] = value
            return value

        if ctx.ID():
            if ctx.ID().getText() in self.args_map:
                return self.args_map[ctx.ID().getText()]
            else:
                raise Exception("%s not define" % ctx.getText())

        if ctx.LPAREN():
            return self.visit(ctx.expr(0))

        if ctx.POWER():
            return self.visitExpr(ctx.expr(0)) ** self.visitExpr(ctx.expr(1))

        if ctx.MINUS() and not ctx.expr(1):
            return -1 * self.visit(ctx.expr(0))

        if ctx.MUL():
            return self.visitExpr(ctx.expr(0)) * self.visitExpr(ctx.expr(1))

        if ctx.DIV():
            return self.visitExpr(ctx.expr(0)) / self.visitExpr(ctx.expr(1))

        if ctx.PLUS():
            return self.visitExpr(ctx.expr(0)) + self.visitExpr(ctx.expr(1))

        if ctx.MINUS():
            return self.visitExpr(ctx.expr(0)) - self.visitExpr(ctx.expr(1))
