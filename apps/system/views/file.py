# -*- coding:utf-8 -*-
# @FileName  :file.py
# @Time      :2023/1/6 15:40
# @Author    : yuhaiping
from apps.system.models import SystemFileManage
from apps.utils.error_code import ErrorCode
from apps.utils.minio_helper import MinIOHelper
from apps.utils.response import APIResponse
from apps.utils.validation import require_param


@require_param({
    'method': 'GET',
    'desc': u'获取文件',
    'params': [
    ]
})
def get_file(request, file_id):
    file_obj = SystemFileManage.objects.filter(file_id=file_id).first()
    if not file_obj:
        APIResponse(error=ErrorCode.API_FILE_NOT_EXIST_ERROR)

    file_url = MinIOHelper().get_file_pre_url(file_obj.file_id)

    data = {
        "file_url": file_url
    }

    return APIResponse(data)
