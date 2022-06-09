# -*- encoding: utf-8 -*-
'''
@create_time: 2022/06/08 17:16:52
@author: lichunyu
'''
from typing import TYPE_CHECKING

from .utils import _LazyModule


__version__ = "0.2.0"


_import_structure = {
    "engine.engine": [
        "Engine",
        "get_app"
    ],
    "core.core": [
        "Graph",
        "node_register"
    ]
}


if TYPE_CHECKING:
    from .engine.engine import Engine, get_app
    from .core.core import Graph, node_register
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )