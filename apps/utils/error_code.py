# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ErrorCode(object):
    """
    Error code
    """
    SUCCESS = ('200', u'success')
    SUCCESS_GATEWAY = ('000', u'success')
    SYSTEM_ERROR = ('999', u'系统繁忙')
    AUTH_ERROR = ('1001001', u'无权操作')
    API_PARAMS_ERROR = ('1001002', u'API参数缺失或错误')
    API_REQUEST_METHOD_ERROR = ('1001003', u'请求方法错误')

