#ubuntu-with-python36

#xuqinghan @ 20170903

#ubuntu16.04+python36


#docker build -t ubuntu-with-python .
#docker tag ubuntu-with-python xuqinghan/ubuntu-with-python:3

#docker tag ubuntu-with-python xuqinghan/ubuntu-with-python:3.6

#docker tag ubuntu-with-python xuqinghan/ubuntu-with-python:3.6.2

#docker tag ubuntu-with-python xuqinghan/ubuntu-with-python:latest



FROM ubuntu

#python3.6  http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/
#RUN cp ./sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates curl wget software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y python3.6
RUN apt install -y python3.6-dev
RUN apt install -y python3.6-venv
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
#RUN ln -s /usr/bin/python3.6 /usr/local/bin/python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
RUN update-alternatives --config python3

#RUN rm /usr/bin/python3
#RUN ln -s python3.5 /usr/bin/python3
