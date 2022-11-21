# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/21 13:52:48
@author: lichunyu
'''
from msf import node_register


@node_register()
def resource(x):
    response = x.resource["resource"].test_resource
    return response