# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/18 13:54:34
@author: lichunyu
'''

from msf import node_register



@node_register()
def test_node_via_print(**kwds):
    param = kwds.get('ids', [])
    result = {
        'result': param
    }
    return result