#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 17:55
# @Author  : Jason Yu
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from .duplicate_limit import duplicate_limit
from.required_fields import required_fields

func_dict = {
    "重复数量": duplicate_limit,
    "必填项": required_fields
}
