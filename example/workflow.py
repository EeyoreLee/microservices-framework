# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/17 15:13:55
@author: lichunyu
'''

config = {
    "health": {
        "flow": ["health"]
    },
    "resource": {
        "flow": ["resource"]
    },
    "resource_multi_node": {
        "flow": ["placeholder_1", "placeholder_2", "resource"]
    },
    "context": {
        "flow": ["context_1", "context_2"]
    },
    "param": {
        "flow": ["param_1"]
    },
    "param_multi_node": {
        "flow": ["placeholder_1", "placeholder_2", "param_1"]
    },
    "args": {
        "flow": ["args_1"],
        "args": {
            "args_1": {
                "arg_1": "test arg_1",
                "arg_2": "test arg_2"
            }
        }
    },
    "args_multi_node": {
        "flow": ["args_1", "args_2"],
        "args": {
            "args_1": {
                "arg_1": "test arg_1"
            },
            "args_2": {
                "arg_2": "test arg_2"
            }
        }
    }
}