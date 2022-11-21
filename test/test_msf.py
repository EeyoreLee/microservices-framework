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

import pytest

from example.run import main


logger = logging.getLogger()


@pytest.fixture()
def app():
    app = main()
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


def test_edit_user(client):
    response = client.post("/test", data={
        "name": "Flask",
        "theme": "dark"
    })
    logger.info(response.text)
    assert response.status_code == 200