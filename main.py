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


def main(script_name):
    filepath = f"scripts/{script_name}"
    inputs = FileStream(filepath)
    lexer = FanLexer(inputs)
    stream = CommonTokenStream(lexer)
    parser = FanParser(stream)
    tree = parser.prog()

    visitor = FanLangVisitor()

    return visitor.visit(tree)


if __name__ == '__main__':
    main('test.fan')