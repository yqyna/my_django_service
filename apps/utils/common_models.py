# -*- coding:utf-8 -*-
# @FileName  :common_models.py
# @Time      :2022/11/21 15:57
# @Author    : yuhaiping

from collections import namedtuple

from django.db import models
from django.forms.models import model_to_dict


class AbstractAfterSaveModel(models.Model):
    """
    class 包含保存后操作的基础类
    """

    class Meta:
        abstract = True

    pre_cache_fields = []

    def __init__(self, *args, **kwargs):
        super(AbstractAfterSaveModel, self).__init__(*args, **kwargs)
        self.__pre = model_to_dict(self, fields=self.__class__.pre_cache_fields)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        created = self._state.adding
        super(AbstractAfterSaveModel, self).save(force_insert, force_update, *args, **kwargs)
        if self.__class__.pre_cache_fields:
            res = self.__pre
            fields = set(self.__class__.pre_cache_fields).intersection(set(res.keys()))
            PreClass = namedtuple('{}Pre'.format(self.__class__.__name__), list(fields))
            self.after_save(PreClass(**res), created)
            self.__pre = model_to_dict(self, fields=self.__class__.pre_cache_fields)

    def after_save(self, pre, created=False):
        pass
