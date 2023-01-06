# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse

from apps.utils.error_code import ErrorCode


class APIResponse(HttpResponse):

    def __init__(self, data=None, error=None, *args, **kwargs):

        rsp = {}
        if error is not None:
            if type(error) == dict:
                rsp.update(error)
            else:
                rsp.update({'code': error[0], 'msg': error[1]})
        else:
            success_data = ErrorCode.SUCCESS
            rsp.update({'code': success_data[0], 'msg': success_data[1], 'data': {}})

        if data is not None:
            rsp['data'] = data
        rsp['code'] = int(rsp['code'])
        super(APIResponse, self).__init__(json.dumps(rsp, default=str), content_type='application/json', *args, **kwargs)


class APIGatewayResponse(HttpResponse):

    def __init__(self, data=None, error=None, *args, **kwargs):

        rsp = {}
        if error is not None:
            if type(error) == dict:
                rsp.update(error)
            else:
                rsp.update({'code': error[0], 'msg': error[1]})
        else:
            success_data = ErrorCode.SUCCESS_GATEWAY
            rsp.update({'code': success_data[0], 'msg': success_data[1], 'data': {}})

        if data is not None:
            rsp['data'] = data
        rsp['subcode'] = f"1{str(abs(int(rsp['code'])))[:5].ljust(5, '0')}"
        super(APIGatewayResponse, self).__init__(json.dumps(rsp), content_type='application/json', *args, **kwargs)


class WeChatResponse(HttpResponse):

    def __init__(self, data=None, error=None, *args, **kwargs):

        rsp = ""
        if data is not None:
            rsp = data.get('res')
        super(WeChatResponse, self).__init__(rsp, content_type='text/html;charset=utf-8', *args, **kwargs)
