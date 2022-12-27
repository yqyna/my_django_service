# -*- coding:utf-8 -*-
# @FileName  :use_mango_db_example.py
# @Time      :2022/11/10 17:32
# @Author    : yuhaiping

import pymongo
conn = pymongo.MongoClient('mongodb://user:password@ip:port')
database = conn.item

collection = database.zhangsan


# collection.insert_many([
#      {'name': '赵小三','age':20,'address':'北京'},
#    {'name': '钱小四','age':21,'address':'上海'},
#    {'name': '孙小五','age':20,'address':'山东'},
#    {'name': '李小六','age':23,'address':'河北'},
#    {'name': '欧阳小七','age':24,'address':'杭州'}
#  ])
x = collection.find_one()
print(x)

rows = collection.find()
for row in rows:
    print(row)