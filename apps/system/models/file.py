# -*- coding:utf-8 -*-
# @FileName  :file.py
# @Time      :2023/1/6 15:11
# @Author    : yuhaiping

from django.db import models
from django.forms import model_to_dict

from apps.utils.common_models import gen_id, AbstractTimeModel


class SystemFileManage(AbstractTimeModel):
    """
    文件管理表
    """
    file_id = models.CharField(max_length=255, verbose_name="文件ID", default=gen_id, help_text="文件ID")
    file_name = models.CharField(max_length=255, verbose_name="文件名称", null=True, blank=True, help_text="文件名称")
    file_type = models.CharField(max_length=255, verbose_name="文件类型", null=True, blank=True, help_text="文件类型")
    file_size = models.CharField(max_length=64, verbose_name="文件大小", null=True, blank=True, help_text="文件大小")
    # 本地、阿里云、腾讯云..
    address = models.CharField(max_length=64, verbose_name="存储位置", null=True, blank=True, help_text="存储位置")
    source = models.CharField(max_length=16, verbose_name="文件来源", null=True, blank=True, help_text="文件来源")
    is_success = models.BooleanField(default=0, verbose_name='是否上传成功')

    class Meta:
        app_label = 'system'
        db_table = 'system_file_manage'
        verbose_name = '文件管理表'
        verbose_name_plural = verbose_name

    def to_dict(self):
        dict_info = model_to_dict(self)
        dict_info['create_time'] = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        dict_info['modify_time'] = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return dict_info

