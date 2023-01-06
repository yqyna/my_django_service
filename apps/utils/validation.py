# -*- coding:utf-8 -*-
# @FileName  :validation.py
# @Time      :2023/1/6 15:46
# @Author    : yuhaiping
import re
import copy
import json
from functools import wraps

from django.utils.decorators import available_attrs

from apps.utils.error_code import ErrorCode
from apps.utils.response import APIResponse


def require_param(parameters):
    """
    validate required param

    :param parameters:
    :return:
    """

    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            valid = True
            error = copy.copy(ErrorCode.API_PARAMS_ERROR)
            method = parameters['method']
            request_params = parameters['params']
            if method == 'GET':
                params = request.GET.dict()
            elif method == 'POST':
                if request.content_type == 'application/json':
                    try:
                        params = json.loads(request.body)
                    except Exception as e:
                        print(e)
                        print('======== request body: ', request.body)
                        params = {}
                else:
                    params = request.POST.dict()
            else:
                return APIResponse(error=ErrorCode.API_REQUEST_METHOD_ERROR)

            err_param = {}
            for item in request_params:
                # 检查参数是否必须
                name = item['name']
                required = item['must']
                regex = item['regex']
                desc = item['desc']
                desc_is_special = item.get("desc_is_special")

                if required is True and name not in params:
                    valid = False
                    err_param['name'] = name
                    err_param['info'] = u'%s缺失！' % desc
                    break
                # 检查参数格式是否合法
                if name in params:
                    value = params[name]
                    if (required is False) and (value == '' or value is None):
                        continue
                    # 对regex为'.*'的字段不检查
                    if regex == '.*':
                        continue
                    if not re.match(regex, str(value), re.DOTALL):
                        valid = False
                        err_param['name'] = name
                        err_param['info'] = u'%s格式错误或不合法！' % desc
                        if desc_is_special:
                            err_param['info'] = desc
                        break
            if valid:
                request.params = params
                return func(request, *args, **kwargs)
            else:
                print(err_param.items())
                return APIResponse(error=(error[0], err_param['info']))
        return inner

    return decorator
