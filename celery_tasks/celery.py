# -*- coding:utf-8 -*-
# @FileName  :celery.py
# @Time      :2022/11/2 15:44
# @Author    : yuhaiping

from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR_PARENT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, BASE_DIR_PARENT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_service.settings')

app = Celery('tasks')
app.config_from_object('celery_tasks.celery_config', namespace='CELERY')
app.autodiscover_tasks()
