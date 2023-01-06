# -*- coding:utf-8 -*-
# @FileName  :file.py
# @Time      :2023/1/6 15:40
# @Author    : yuhaiping
from apps.utils.response import APIResponse
from apps.utils.validation import require_param


@require_param({
    'method': 'GET',
    'desc': u'获取文件',
    'params': [
        {'name': 'file', 'must': False, 'regex': '.*', 'desc': '文件'},
    ]
})
def get_file(request, file_id):
    params = request.params
    print(params)
    print(file_id)

    return APIResponse()
