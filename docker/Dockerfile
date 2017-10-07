#quotation api for lazyman35
#xuqinghan @ 201701005

#启动container


#docker run --name quotation_api -itd -p 5000:5000 -v /home/xuqinghan/lazyman35/quotation:/code quotation_dev:latest

#启动python3
#docker start quotation_api
#docker attach quotation_api
# cd /code
# python3 main.py

#删除容器，要加-v 
#docker rm quotation_api
#docker rmi quotation
#删除全部不运行的容器
#docker rm $(docker ps -a -q) -v


#创建镜像
#docker build -t quotation .

FROM ubuntu-with-python
LABEL author="lazyman"

#代码复制过来后的路径
RUN mkdir /code
WORKDIR /code

#安装需要的python库
RUN pip3 install flask
RUN pip3 install flask-sqlalchemy
RUN pip3 install flask_restful