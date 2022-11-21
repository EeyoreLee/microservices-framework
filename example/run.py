# -*- encoding: utf-8 -*-
'''
@create_time: 2021/11/18 13:58:32
@author: lichunyu
'''
import sys
sys.path.append('.')

from example.workflow_conf import NODE_CONF, PATH_CONF
from .nodes import *
from msf import Engine


class ResourceTest(object):

    def __init__(self) -> None:
        super().__init__()
        self.apple = 'apppppp'

def main():

    config = {
        'NODE_CONF': NODE_CONF,
        'PATH_CONF': PATH_CONF
    }
    resource_apple = ResourceTest()
    resource = {'test_rsc': resource_apple}
    engine = Engine(config, resource=resource)
    # engine.run(host='0.0.0.0', port='42000')
    return engine.get_app()


if __name__ == "__main__":
    app = main()
    app.run()