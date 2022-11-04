FROM python:3.8.12
LABEL AUTHOR="yuhaiping"
MAINTAINER yqyn
ENV PYTHONUNBUFFERED 1
VOLUME "/app"
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN mkdir -p /var/log/supervisor &&
RUN mkdir -p /run/supervisor &&
RUN chmod 777 /var/run &&
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple