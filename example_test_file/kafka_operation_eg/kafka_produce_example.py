# -*- coding:utf-8 -*-
# @FileName  :kafka_produce_example.py
# @Time      :2022/11/21 15:03
# @Author    : yuhaiping

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers=['192.168.31.22:9092']
)
msg_dict = {
    "operatorId": "test",  # 公交公司ID
    "terminalId": "123",  # 设备Id
    "terminalCode": "123",  # 设备编码（使用车辆ID）
    "terminalNo": "1",  # 同一车辆内terminal序号从1开始
}

producer.send("text1", msg_dict)
producer.close()
