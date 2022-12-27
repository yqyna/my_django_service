# -*- coding:utf-8 -*-
# @FileName  :kafka_consumer_example.py
# @Time      :2022/11/21 15:02
# @Author    : yuhaiping

from kafka import KafkaConsumer

consumer = KafkaConsumer('text1', bootstrap_servers='192.168.31.22:9092')
for msg in consumer:
    print(msg.value.decode())
