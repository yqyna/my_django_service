# -*- coding:utf-8 -*-
# @FileName  :user.py
# @Time      :2022/12/27 9:31
# @Author    : yuhaiping
import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.app_user import user_settings
from apps.utils.common_models import AbstractTimeModel


class Users(AbstractUser, AbstractTimeModel):

    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name="用户账号", help_text="用户账号")
    email = models.EmailField(max_length=255, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    mobile = models.CharField(max_length=255, verbose_name="电话", null=True, blank=True, help_text="电话")
    avatar = models.CharField(max_length=255, verbose_name="头像", null=True, blank=True, help_text="头像")
    name = models.CharField(max_length=40, verbose_name="姓名", help_text="姓名")
    nickname = models.CharField(default='', max_length=150, verbose_name="昵称")
    open_id = models.CharField(default='', max_length=255, verbose_name='给外部应用使用的唯一用户标识:open_id', db_index=True)
    account_state = models.PositiveSmallIntegerField(default=0, verbose_name=u'账号状态 0-正常 1-停用')
    user_type = models.CharField(default=user_settings.UserTypeEnum.UNKNOWN, max_length=128,
                                 choices=user_settings.USER_TYPE_CHOICES, verbose_name=u'用户所属角色')

    source = models.PositiveSmallIntegerField(default=user_settings.UserSourceEnum.UNKNOWN,
                                              choices=user_settings.USER_SOURCE_CHOICES,
                                              verbose_name=u'用户注册来源')
    init_password = models.CharField(default='', max_length=128, verbose_name='初始密码')
    expire_time = models.CharField(default='', max_length=128, verbose_name='过期时间')

    def set_password(self, raw_password):
        super().set_password(hashlib.md5(raw_password.encode(encoding="UTF-8")).hexdigest())

    class Meta:
        app_label = 'app_user'
        db_table = 'app_base_users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ("-create_time",)


