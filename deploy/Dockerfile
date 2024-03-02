FROM ubuntu:20.04
# 这里要替换 your_name 为您的名字, 和your_email 为您的Email
MAINTAINER mercury <mercury@run.run>
# 更新源
# 设置为中国国内源
RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list && sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip git supervisor
#RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir flask==1.1.4 gunicorn -i https://pypi.mirrors.ustc.edu.cn/simple

RUN apt-get autoclean && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apk/* && apt-get remove -y python3-pip && apt-get autoremove -y

COPY ./start.sh /home/
ENTRYPOINT ["sh", "/home/start.sh"]