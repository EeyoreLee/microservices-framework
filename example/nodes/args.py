# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/21 14:26:00
@author: lichunyu
'''
import logging

from msf import node_register


@node_register()
def args_1(x):
    args = x.args
    cxt = x.context
    cxt["args"] = args
    return args


@node_register()
def args_2(x):
    args = x.args
    cxt = x.context
    return {**args, **cxt.get("args", {})}
