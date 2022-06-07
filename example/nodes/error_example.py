from msf.core.core import node_register

import torch


@node_register()
def deprecated_func(**kwds):
    return None