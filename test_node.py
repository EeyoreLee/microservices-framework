from msf.core.core import Node, NodeConfig, __NodeList, node_register


config = {
    'module': 'b',
    'args': '',
    'description': 'test'
}

@node_register(**config)
def test_node_via_print(text):
    print(text)
    return text


pass