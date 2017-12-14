FROM alpine:latest

RUN apk update && apk upgrade && apk add bash 
RUN apk add python3

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN rm -rf /var/cache/apk/*

ADD db.sqlite3 /code
ADD manage.py /code
ADD moikorg_site /code
ADD sonnen /code


ENTRYPOINT ["/usr/bin/python3"]
CMD ["manage.py runserver 8000"]
