# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/17 15:05:43
@author: lichunyu
'''
from functools import wraps
from typing import Any

_NodeList = {}


class GraphConfig(object):

    def __init__(self, config:dict) -> None:
        """创建图配置

        :param config: 包含NODE_CONF和PATH_CONF
        :type config: dict
        """        
        super().__init__()
        self.node_conf: dict = config.get('NODE_CONF', {}) if isinstance(config, dict) else {}
        self.path_conf: dict = config.get('PATH_CONF', {}) if isinstance(config, dict) else {}


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

    def forward(self, *args, **kwds):
        return 'response success'

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.forward(*args, **kwds)

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
        node_conf = self.config.node_conf
        nodes = {}
        for k, v in node_conf.items():
            if k in _NodeList:
                raise Exception('CONF声明的节点已被注册')
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
        self.flow = []
        self.nodes = []
        self.build_flow(nodes)

    def build_flow(self, nodes):
        flow_conf = self.config.flow
        for n in flow_conf:
            self.flow.append(nodes[n])
            self.nodes.append(nodes[n])

    def walk(self, **kwds):
        factor = None
        for n in self.flow:
            factor = n(factor=factor, **kwds)
        return factor

    def __call__(self,**kwds):
        return self.walk(**kwds)


def node_register(name=None, module=None, args=None, description=None, config=None):

    def decorator(func):
        config = {
            'module': module,
            'args': args,
            'description': description
        }
        node = Node(config)

        @wraps(func)
        def wrapper(*args, **kwds):
            return func(*args, **kwds)

        node.forward = wrapper
        _NodeList[func.__name__ if name is None else name] = node
        return wrapper

    return decorator

