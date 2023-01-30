# -*- coding:utf-8 -*-
# @FileName  :use_chatgpt_example.py
# @Time      :2023/1/30 11:02
# @Author    : yuhaiping

import openai

openai.api_key = "YOUR_API_KEY"

model_engine = "text-davinci-002"
prompt = "怎么提升自己的代码水平"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)
