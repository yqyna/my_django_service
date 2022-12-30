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

# Download file
client.fget_object('test', 'IMG_1162.MOV', 'IMG_1162.MOV')

# 1.When don't set param content_type and use fput_object func to upload picture successful,
# then use func presigned_get_object to get the url which can't preview in browser but download picture by browser
client.fput_object('test', 'test1.jpeg', 'test1.jpeg')
url = client.presigned_get_object('test', 'test1.jpeg')
print(" url can't preview in browser:", url)

# 2.When set param content_type and use fput_object func to upload picture successful,
# then use func presigned_get_object to get the url which can preview in browser
client.fput_object('test', 'test2.jpeg', 'test2.jpeg', content_type="image/jpeg")
url = client.presigned_get_object('test', 'test2.jpeg')
print("url can preview in browser:", url)
