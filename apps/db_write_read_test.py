# -*- coding:utf-8 -*-
# @FileName  :db_write_read_test.py
# @Time      :2023/1/10 9:47
# @Author    : yuhaiping

# Test DB read write separation

import os
import sys

import django


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_service.settings")
django.setup()

from apps.system.models import SystemFileManage


# file_obj = SystemFileManage.objects.all()
create_info = {}
file_obj = SystemFileManage.objects.create(**create_info)
print(file_obj)
