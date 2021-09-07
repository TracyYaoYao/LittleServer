FROM python:alpine

COPY . /src

ENV SECRET_KEY=TEST_SECRET_KEY \
    SECRET_ID=TEST_SECRET_ID

RUN apk add --no-cache build-base libffi-dev openssl-dev mariadb-dev netcat-openbsd && \
    pip install --upgrade pip && \
    pip install -r /src/requirements.txt && \
    cd /src && \
    cp hack.sh /usr/sbin/hack

WORKDIR /src