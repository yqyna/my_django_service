# -*- coding:utf-8 -*-
# @FileName  :minio_helper.py
# @Time      :2022/12/30 15:50
# @Author    : yuhaiping
from minio import Minio

from django.conf import settings as django_settings


class MinIOHelper(object):
    """
    MinIO工具类
    """

    def __init__(self, host=django_settings.MINIO_HOST, access_key=django_settings.MINIO_ACCESS_KEY,
                 secret_key=django_settings.MINIO_SECRET_KEY, bucket=django_settings.MINIO_BUCKET,
                 save_path=""):
        self.host = host
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket
        self.save_path = save_path
        self.client = Minio(
            host,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )

    def file_download(self, file_id):
        """
        download file by file_id
        save_path default value "" means current file path

        :return:
        """

        self.client.fget_object(self.bucket, file_id, self.save_path)

        return True

    def get_file_pre_url(self, file_id):
        """
        get preview url by file_id

        :param file_id:
        :return:
        """
        pre_url = self.client.presigned_get_object(self.bucket, file_id)
        return pre_url


if __name__ == '__main__':
    # client.fget_object('test', 'test1.jpeg', 'test1.jpeg')
    # MinIOHelper().file_download()
    # client.fput_object('test', 'test2.jpeg', 'test2.jpeg', content_type="image/jpeg")
    # print(client.presigned_get_object('test', 'test2.jpeg'))
    obj = MinIOHelper()
    url = obj.client.presigned_get_object('test', 'test2.jpeg')
    print("url can't preview in browser:", url)

    # client.fput_object('test', 'test1.jpeg', 'test1.jpeg')
    url = obj.client.presigned_get_object('test', 'test1.jpeg')
    print("url can preview in browser:", url)

