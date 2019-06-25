#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 10:20 AM
# @Author  : likaifuismyson@gmail.com
# @Site    : 
# @File    : main.py

from grammar.build.FanLexer import FanLexer
from grammar.build.FanParser import FanParser
from grammar.FanLangVisitor import FanLangVisitor
from antlr4 import *


def run_file(filepath, data=None):
    lexer = FanLexer(FileStream(filepath, encoding="u8"))
    stream = CommonTokenStream(lexer)
    parser = FanParser(stream)
    tree = parser.prog()

    visitor = FanLangVisitor(args_map=data)
    visitor.visit(tree)
    return visitor.return_val


def run(string, data=None):
    if not string.startswith("return "):
        string = "return " + string
    if not string.endswith(";"):
        string = string + ";"

    lexer = FanLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = FanParser(stream)
    tree = parser.prog()

    visitor = FanLangVisitor(args_map=data)
    visitor.visit(tree)
    return visitor.return_val


if __name__ == '__main__':
    # print(run_file("scripts/test.fan", data={"总金额": 100.00, "人数": 3}))
    print(run("总金额/人数 + 100 > 上限 or 总金额 < 50", data={"总金额": 100.00, "人数": 3, "上限": 100}))

    # print(run("100/3 == 33.333333333"))
