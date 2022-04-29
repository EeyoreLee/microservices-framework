# -*- encoding: utf-8 -*-
'''
@create_time: 2022/04/29 14:33:44
@author: lichunyu
'''

import sys
sys.path.append('.')
import logging

import pytest
import requests


@pytest.mark.v0_1_5_3
def test_context():
    data = {"param_typo": "test"}
    resp = requests.post("http://localhost:41000/test", data=data)
    assert resp.status_code == 200