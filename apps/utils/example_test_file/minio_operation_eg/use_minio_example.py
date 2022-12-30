# -*- coding:utf-8 -*-
# @FileName  :use_minio_example.py
# @Time      :2022/12/30 15:42
# @Author    : yuhaiping

from minio import Minio

client = Minio(
    "ip:port",
    access_key="minio_access_key",
    secret_key="minio_secret_key",
    secure=False
)

client.fget_object('test', 'IMG_1162.MOV', 'IMG_1162.MOV')