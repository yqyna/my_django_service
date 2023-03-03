# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/12/26 17:03
# @Author    : yuhaiping

from django.urls import path

from apps.system.views import file, login

app_name = "system"

urlpatterns = [
    path("file/<str:file_id>/get/v1/", file.get_file, name='system_get_file'),
    path("captcha/", login.get_captcha, name='system_get_captcha'),
]
