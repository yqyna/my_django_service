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

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'app_user' or \
                obj2._meta.app_label == 'app_user':
            return True
        elif 'app_user' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        return False
