# -*- coding:utf-8 -*-
# @FileName  :login.py
# @Time      :2023/3/2 16:24
# @Author    : yuhaiping
import uuid

from apps.app_user.models import Users
from apps.utils.error_code import ErrorCode
from apps.utils import captcha
from apps.utils.response import APIResponse


def get_captcha(request):
    """
    获取验证码

    :param request:
    :return:
            eg- {
                  "code": 2000,
                  "data": {
                    "key": 34133,
                    "image_base": "data:image/png;base64,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"
                  },
                  "msg": "success"
                }
    """
    union_key = uuid.uuid4().hex

    code, data = captcha.gen_img_captcha()

    return APIResponse({
                    "key": union_key,
                    "image_base": "data:image/png;base64," + data
                  })


def login_by_password(request):

    # captcha
    # :
    # "bhgf"
    # captchaKey
    # :
    # "797f758b148247ceb5061c1e8c75a162"
    # password
    # :
    # "6512bd43d9caa6e02c990b0a82652dca"
    # username
    # :
    # "11"
    pass
    params = request.params
    captcha = params.get('captcha')
    captchaKey = params.get('captchaKey')
    password = params.get("password")
    username = params.get("username")

    user_obj = Users.objects.filter(username=username)
    if not user_obj:
        return APIResponse(error=ErrorCode.API_USER_NOT_EXIST_ERROR)