# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/21 14:12:50
@author: lichunyu
'''
from msf import node_register


@node_register()
def param_1(x):
    param = x.param
    return param