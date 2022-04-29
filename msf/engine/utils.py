# -*- encoding: utf-8 -*-
'''
@create_time: 2021/12/28 10:32:43
@author: lichunyu
'''
import logging


def param_parse(request):
    content_type = request.content_type
    if "form-data" in content_type or "application/x-www-form-urlencoded" in content_type:
        form_key = [k for k in request.form]
        form_param = {k:request.form[k] for k in form_key}
        return form_param
    elif content_type == "application/json":
            return request.json
    else:
        logging.warning(f"the content_type {content_type} is not currently supported, the parameters cannot be parsed")
        return {}


def response_package(result):
    """根据node返回结果，组织api response

    :param result: node 返回结果
    :type result: [tuple|Any]
    :raises Exception: [description]
    :raises Exception: [description]
    :return: [description]
    :rtype: [type]
    """    
    response = {
        'code': 200,
        'msg': 'success',
        'data': None
    }
    if not isinstance(result, tuple):
        response['data'] = result
        return response

    if len(result) == 1:
        response['data'] = result

    elif len(result) == 2:
        response['data'] = result[0]
        if isinstance(result[1], int):
            response['code'] = result[1]
        elif isinstance(result[1], str):
            response['msg'] = result[1]
        else:
            raise Exception('non std format data')

    elif len(result) == 3:
        response['data'] = result[0]
        if isinstance(result[1], int) and isinstance(result[2], str):
            response['code'] = result[1]
            response['msg'] = result[2]
        elif isinstance(result[1], str) and isinstance(result[2], int):
            response['msg'] = result[1]
            response['code'] = result[2]
        else:
            raise Exception('non std format data')
    else:
        raise Exception('non std format data')

    return response