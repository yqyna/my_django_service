# -*- coding:utf-8 -*-
# @FileName  :tasks.py
# @Time      :2022/11/3 11:03
# @Author    : yuhaiping
from celery_tasks.celery import app as celery_app


@celery_app.task
def test_task():
    print("成功")
    return True, "success"
