# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/18 13:58:32
@author: lichunyu
'''

from msf.engine.engine import Engine
from msf.core.core import Graph, GraphConfig
from example.workflow_conf import NODE_CONF, PATH_CONF
from example.nodes import *


def main():

    config = {
        'NODE_CONF': NODE_CONF,
        'PATH_CONF': PATH_CONF
    }
    graph_config = GraphConfig(config=config)
    graph = Graph(graph_config)
    engine = Engine(graph)
    engine.run(host='0.0.0.0', port='41000')