FROM alpine:latest

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && apk add bash 
RUN apk add python3 python3-dev
RUN apk add mariadb-client-libs mariadb-dev build-base

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

# and remove the tools for building the mysql driver again
RUN apk del python3-dev mariadb-dev build-base 

RUN rm -rf /var/cache/apk/*
