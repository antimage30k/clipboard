FROM ubuntu:18.04
# 这里要替换 your_name 为您的名字, 和your_email 为您的Email
MAINTAINER mercury <mercury@run.run>
# 更新源
RUN apt-get update
# 清除缓存
RUN apt-get autoclean
# 安装python
RUN apt-get install -y python3

# -i https://pypi.tuna.tsinghua.edu.cn/simple
# 装依赖
RUN apt install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN apt-get install -y git supervisor
RUN pip3 install flask==1.1.4 gevent gunicorn

COPY ./start.sh /home/
ENTRYPOINT ["sh", "/home/start.sh"]