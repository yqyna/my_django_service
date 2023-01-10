# -*- coding:utf-8 -*-
# @FileName  :router.py
# @Time      :2023/1/10 9:39
# @Author    : yuhaiping


class Router:
    """
    Database read/write separation Router
    """
    def db_for_read(self, model, **kwargs):
        print("read")
        print(model._meta.app_label)
        return 'default'

    def db_for_write(self, model, **kwargs):
        print("write")
        print(model._meta.app_label)
        return 'write'
