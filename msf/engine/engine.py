# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/17 14:49:28
@author: lichunyu
'''
import json

from flask import Flask, request

from msf.core.core import Graph
from msf.engine.utils import response_package, param_parse


class Engine(object):

    def __init__(self, graph: Graph=None, app=None, resource:dict=None, name=__name__) -> None:
        super().__init__()
        self.graph = graph if isinstance(graph, Graph) else Graph(graph)
        self.resource = resource if resource is not None else {}
        self.init_app(app=app, name=name)
        self.param_parse = param_parse
        self.response_package = response_package

    def flow_mixin(self, path):
        param = self.param_parse(request)
        output = self.graph[path].walk(_resource=self.resource, _param=param)
        output = self.response_package(output)
        return json.dumps(output, ensure_ascii=False)

    def init_app(self, app, name):
        self.app = Flask(name) if app is None else app
        # self.app.register_error_handler()
        self.app.route('/<path>', methods=['POST'])(self.flow_mixin)

    def get_app(self):
        return self.app

    def run(self, *args, **kwds):
        self.app.run(*args, **kwds)


def get_app(engine: Engine):
    return engine.app