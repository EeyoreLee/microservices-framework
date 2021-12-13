# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/17 14:49:28
@author: lichunyu
'''
import json

from msf.core.core import Graph
from flask import Flask, request


class Engine(object):

    def __init__(self, graph: Graph=None, resource:dict=None, name=__name__) -> None:
        super().__init__()
        self.graph = graph if isinstance(graph, Graph) else Graph(graph)
        self.resource = resource if resource is not None else {}
        self.create_app(name)

    def flow_mixin(self, path):
        param = request.json
        result = self.graph[path].walk(_resource=self.resource, **param).get('result', '')
        return json.dumps(result, ensure_ascii=False)

    def create_app(self, name):
        self.app = Flask(name)
        self.app.route('/<path>', methods=['POST'])(self.flow_mixin)
        return self.app

    def run(self, *args, **kwds):
        self.app.run(*args, **kwds)