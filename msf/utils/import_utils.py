# -*- encoding: utf-8 -*-
'''
@create_time: 2022/06/08 17:51:25
@author: lichunyu
'''
import sys
import importlib
import os
from itertools import chain
import re

from . import logger


ModuleType = type(sys)


class _LazyModule(ModuleType):

    def __init__(self, name, module_file, import_structure, module_spec=None, extra_objects=None):
        super().__init__(name)
        self._modules = set(import_structure.keys())
        self._class_to_module = {}
        for key, values in import_structure.items():
            for value in values:
                self._class_to_module[value] = key
        self.__all__ = list(import_structure.keys()) + list(chain(*import_structure.values()))
        self.__file__ = module_file
        self.__spec__ = module_spec
        self.__path__ = [os.path.dirname(module_file)]
        self._objects = {} if extra_objects is None else extra_objects
        self._name = name
        self._import_structure = import_structure

    def __dir__(self):
        result = super().__dir__()
        for attr in self.__all__:
            if attr not in result:
                result.append(attr)
        return result

    def __getattr__(self, name: str):
        if name in self._objects:
            return self._objects[name]
        if name in self._modules:
            value = self._get_module(name)
        elif name in self._class_to_module.keys():
            module = self._get_module(self._class_to_module[name])
            value = getattr(module, name)
        else:
            raise AttributeError(f"module {self.__name__} has no attribute {name}")

        setattr(self, name, value)
        return value

    def _get_module(self, module_name: str):
        try:
            return importlib.import_module("." + module_name, self.__name__)
        except Exception as e:
            raise RuntimeError(
                f"Failed to import {self.__name__}.{module_name} because of the following error (look up to see its traceback):\n{e}"
            ) from e

    def __reduce__(self):
        return (self.__class__, (self._name, self.__file__, self._import_structure))


def load_register_node(dir_path, ignores=None):
    ignore_list = ['__pycache__', '__MACOSX', '.DS_Store']
    ignore_list = ignore_list + ignores if ignores else ignore_list
    for root, dirs, files in os.walk(dir_path):
        _, dirname = os.path.split(root)
        if dirname in ignore_list:
            continue
        for f in (set(files) - set(ignore_list)):
            file_path = os.path.join(root, f)
            with open(file_path) as fd:
                s = fd.read()
            if re.search('node_register', s):
                module_str = os.path.split(dir_path)[1] + '.' + dirname + '.' + f.split('.')[0]
                logger.debug(f"auto import node: {module_str}")
                importlib.import_module(module_str)