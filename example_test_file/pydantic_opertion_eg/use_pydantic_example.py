# -*- coding:utf-8 -*-
# @FileName  :use_pydantic_example.py
# @Time      :2022/11/10 17:24
# @Author    : yuhaiping

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'yo yo'
    birth: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'birth': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.dict())  # dict()

# external_data1 = {
#     'id': 'aaa',
#     'birth': '2019-06-01 12:22',
#     'friends': [1, 2, '3'],
# }
# user1 = User(
#     **external_data1
# )
# user.dict()

from pydantic import ValidationError

external_data1 = {
    'id': 'aaa',
    'birth': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

try:
    user1 = User(**external_data1)
except ValidationError as e:
    print(e.json())
