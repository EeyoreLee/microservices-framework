# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/17 15:05:43
@author: lichunyu
'''
from functools import wraps
from typing import Any
from dataclasses import dataclass, field


_NodeList = {}


@dataclass
class NodeInput:  # XXX rename it

    context: dict = field(default_factory=dict, metadata={"help": "context"})
    param: dict = field(default_factory=dict, metadata={"help": "body from request"})
    resource: dict = field(default_factory=dict, metadata={
        "help": "Store resources that need to be loaded but do not want to be loaded temporarily with the request"
    })
    args: dict = field(default_factory=dict, metadata={"help": "args from path config"})


class GraphConfig(object):

    def __init__(self, config:dict) -> None:
        super().__init__()
        # self.node_conf: dict = config.get('NODE_CONF', {}) if isinstance(config, dict) else {}  # XXX Creating nodes via configuration is temporarily deprecated
        # self.path_conf: dict = config.get('PATH_CONF', {}) if isinstance(config, dict) else {}
        self.path_conf = config


class NodeConfig(object):

    def __init__(self, config:dict) -> None:
        super().__init__()
        self.module = config.get('module', None) if isinstance(config, dict) else None
        self.args: dict = config.get('args', {}) if isinstance(config, dict) else {}
        self.description = config.get('description', None) if isinstance(config, dict) else None


class PathConfig(object):

    def __init__(self, config:dict) -> None:
        super().__init__()
        self.flow = config.get('flow', None) if isinstance(config, dict) else None
        self.description = config.get('description', None) if isinstance(config, dict) else None


class Node(object):

    def __init__(self, config: NodeConfig) -> None:
        super().__init__()
        self.config = config if isinstance(config, NodeConfig) else NodeConfig(config)

    def forward(self, node_input):
        raise NotImplementedError()

    def __call__(self, node_input) -> Any:
        return self.forward(node_input)

    # @classmethod
    # def node_register(cls, config):
    #     node_instance = cls(config)
    #     def decorator(func):
    #         node_instance.forward = func
    #         return func
    #     return decorator


class Graph(object):

    def __init__(self, config: GraphConfig) -> None:
        super().__init__()
        self.config = config if isinstance(config, GraphConfig) else GraphConfig(config)
        self.paths = None
        self.nodes = None
        self.build_node()
        self.build_path()

    def build_node(self):
        # node_conf = self.config.node_conf  # XXX Creating nodes via configuration is temporarily deprecated
        node_conf = {}
        nodes = {}
        for k, v in node_conf.items():
            if k in _NodeList:
                raise Exception("Node has been registered")
            nodes[k] = Node(v)
        nodes.update(_NodeList)
        self.nodes = nodes

    def build_path(self):
        path_conf = self.config.path_conf
        paths = {}
        for k, v in path_conf.items():
            paths[k] = Path(v, self.nodes)
        self.paths = paths

    def __getitem__(self, key):
        return self.paths[key]


class Path(object):

    def __init__(self, config, nodes) -> None:
        super().__init__()
        self.config = config if isinstance(config, PathConfig) else PathConfig(config)
        self.flow = {}
        self._args = config.get('args', {})
        self.global_args = config.get('global_args', {})
        self.nodes = []
        self.build_flow(nodes)

    def build_flow(self, nodes):
        flow_conf = self.config.flow
        for n in flow_conf:
            self.flow[n] = nodes[n]
            self.nodes.append(nodes[n])

    def walk(self, node_input):
        for name, node in self.flow.items():
            node_input.args: dict = self._args.get(name, {})
            output = node(node_input)
        return output

    def __call__(self, node_input):
        return self.walk(node_input)


def node_register(name=None, module=None, args=None, description=None, config=None):

    def decorator(func):
        config = {
            'module': module,
            'args': args,
            'description': description
        }
        node = Node(config)

        @wraps(func)
        def wrapper(*_args, **kwds):
            return func(*_args, **kwds)

        node.forward = wrapper
        _NodeList[func.__name__ if name is None else name] = node
        return wrapper

    return decorator

