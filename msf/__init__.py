# -*- encoding: utf-8 -*-
'''
@create_time: 2022/06/08 17:16:52
@author: lichunyu
'''
from typing import TYPE_CHECKING

from .utils import _LazyModule


__version__ = "0.2.0"


_import_structure = {
    "engine": [
        "Engine",
        "get_app"
    ],
    "core": [
        "Graph",
        "node_register"
    ],
    "utils.import_utils": [
        "load_register_node"
    ]
}


if TYPE_CHECKING:
    from .engine import Engine, get_app
    from .core import Graph, node_register
    from .utils.import_utils import load_register_node
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )