# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/18 13:54:34
@author: lichunyu
'''
import logging

from msf import node_register


logger = logging.getLogger()


@node_register()
def test_node_via_print(x):
    logger.info(x)
    x.context["test_words"] = "test_word"
    # context = kwds.get('_context')
    # context['test_tmp_var'] = 'test'
    # resource = kwds.get('_resource', {})
    # resource_apple = resource.get('test_rsc')
    # param = kwds.get('ids', [])
    # result = {
    #     'result': param
    # }
    # print(resource_apple.apple)
    return 


@node_register()
def test_context(x):
    logger.info(x.context.get("test_words"))