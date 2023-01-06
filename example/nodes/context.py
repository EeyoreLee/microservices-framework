# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/21 14:06:28
@author: lichunyu
'''
from msf import node_register


@node_register()
def context_1(x):
    context = x.context
    context["context"] = "context test"
    return


@node_register()
def context_2(x):
    context = x.context
    result = context["context"]
    return result