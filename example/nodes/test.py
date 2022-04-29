# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/18 13:54:34
@author: lichunyu
'''

from msf import node_register



@node_register()
def test_node_via_print(**kwds):
    print(kwds)
    context = kwds.get('_context')
    context['test_tmp_var'] = 'test'
    resource = kwds.get('_resource', {})
    resource_apple = resource.get('test_rsc')
    param = kwds.get('ids', [])
    result = {
        'result': param
    }
    print(resource_apple.apple)
    return result


@node_register()
def test_context(**kwds):
    context = kwds.get('_context')
    print(context)