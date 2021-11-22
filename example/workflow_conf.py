# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/17 15:13:55
@author: lichunyu
'''


NODE_CONF = {
    'a': {
        "module": "example.nodes.test",
        "args": [],
        "description": ""
    }
}


PATH_CONF = {
    "test": {
        "flow": ['test_node_via_print'], 
        "description": ""
    }
}