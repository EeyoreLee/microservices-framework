# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/15 15:37:22
@author: lichunyu
'''
from dataclasses import dataclass, field


@dataclass
class NodeInput:  # XXX rename it

    context: dict = field(default_factory=dict, metadata={"help": "context"})
    param: dict = field(default_factory=dict, metadata={"help": "body from request"})
    resource: dict = field(default_factory=dict, metadata={
        "help": "Store resources that need to be loaded but do not want to be loaded temporarily with the request"
    })
    args: dict = field(default_factory=dict, metadata={"help": "args from path config"})