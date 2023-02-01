# -*- coding:utf-8 -*-
# @FileName  :common_config.py
# @Time      :2023/1/30 14:16
# @Author    : yuhaiping

from django.db import models
from django.forms import model_to_dict

from apps.utils.common_models import gen_id, AbstractTimeModel, AbstractStateModel


class SystemCommonConfig(AbstractTimeModel, AbstractStateModel):
    """
    系统公共配置管理表
    """
    config_key = models.CharField(max_length=255, verbose_name="配置ID", default=gen_id, help_text="配置ID")
    config_name = models.CharField(max_length=255, verbose_name="配置名称", null=True, blank=True, help_text="配置名称")
    config_type = models.CharField(max_length=255, verbose_name="配置类型", null=True, blank=True, help_text="配置类型")
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    config_value = models.TextField(default='', verbose_name='值')
    remark = models.TextField(default='', verbose_name='描述')
    access_token = models.CharField(max_length=255, verbose_name="授权token", null=True, blank=True, help_text=u"授权token")

    class Meta:
        app_label = 'system'
        db_table = 'system_common_config'
        verbose_name = '系统公共配置管理表'
        verbose_name_plural = verbose_name

    def to_dict(self):
        dict_info = model_to_dict(self)
        dict_info['create_time'] = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        dict_info['modify_time'] = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return dict_info
