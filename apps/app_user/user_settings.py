# -*- coding:utf-8 -*-
# @FileName  :user_settings.py
# @Time      :2022/12/29 17:43
# @Author    : yuhaiping


class UserSourceEnum:
    UNKNOWN = 0


USER_SOURCE_CHOICES = (
    (UserSourceEnum.UNKNOWN, u'未知'),
)


class UserTypeEnum:
    UNKNOWN = 0
    BACKEND_USER = 1
    WEB_USER = 2


USER_TYPE_CHOICES = (
    (UserTypeEnum.UNKNOWN, u'未知'),
    (UserTypeEnum.BACKEND_USER, u'后台用户'),
    (UserTypeEnum.WEB_USER, u'前台用户'),
)

