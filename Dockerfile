FROM alpine:latest

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && apk add bash 
RUN apk add python3

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN rm -rf /var/cache/apk/*
