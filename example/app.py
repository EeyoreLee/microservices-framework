# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/18 13:58:32
@author: lichunyu
'''
import os
import sys
import logging
sys.path.append('.')

from example.workflow import config
from msf import Engine, get_app, load_register_node

# load_register_node(os.path.dirname(__file__))


class ResourceTest(object):

    def __init__(self) -> None:
        super().__init__()
        self.test_resource = {"metadata": "just for resource test"}


def create_engine():
    load_register_node(os.path.dirname(__file__))
    resource = {'resource': ResourceTest()}
    engine = Engine(config, resource=resource)
    return engine


def create_app():
    engine = create_engine()
    app = get_app(engine)
    return app


# app = create_app()


if __name__ == "__main__":
    engine = create_engine()    
    engine.run(host='0.0.0.0', port='42000')