FROM python:3
RUN apt-get update && \
    apt-get -y install mariadb-client
RUN apt -y install mecab libmecab-dev mecab-utils mecab-jumandic-utf8 mecab-naist-jdic python3-mecab
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt