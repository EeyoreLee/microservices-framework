# -*- encoding: utf-8 -*-
'''
@create_time: 2022/11/21 10:20:06
@author: lichunyu
'''
import os
import sys
sys.path.append(".")
sys.path.append("./msf")
import logging
import json

import pytest
from requests import Response

from example.app import create_app


logger = logging.getLogger()


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


# def test_request_example(client):
#     response = client.get("/posts")
#     assert b"<h2>Hello, World!</h2>" in response.data


def test_health(client):
    response: Response = client.post("/health")
    assert response.status_code == 200


def test_resource(client):
    response: Response = client.post("/resource")
    result = json.loads(response.text).get("data", {})
    assert result == {'metadata': 'just for resource test'}


def test_resource_multi_node(client):
    response: Response = client.post("/resource_multi_node")
    result = json.loads(response.text).get("data", {})
    assert result == {'metadata': 'just for resource test'}


def test_context(client):
    response: Response = client.post("/context")
    result = json.loads(response.text).get("data", {})
    assert result == "context test"


def test_param(client):
    data = {
        "param_1": "test_param1",
        "param_2": "test_param2"
    }
    response: Response = client.post("/param", data=data)
    result = json.loads(response.text).get("data", {})
    assert result == data


def test_param_multi_node(client):
    data = {
        "param_1": "test_param1",
        "param_2": "test_param2"
    }
    response: Response = client.post("/param_multi_node", data=data)
    result = json.loads(response.text).get("data", {})
    assert result == data


def test_args(client):
    gt = {
        "arg_1": "test arg_1",
        "arg_2": "test arg_2"
    }
    response: Response = client.post("/args")
    result = json.loads(response.text).get("data", {})
    assert result == gt


def test_args_multi_node(client):
    gt = {
        "arg_1": "test arg_1",
        "arg_2": "test arg_2"
    }
    response: Response = client.post("/args_multi_node")
    result = json.loads(response.text).get("data", {})
    assert result == gt