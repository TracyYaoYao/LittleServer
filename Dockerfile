FROM python:alpine

COPY . /src

ENV SECRET_KEY=TEST_SECRET_KEY \
    SECRET_ID=TEST_SECRET_ID

RUN apk add build-base libffi-dev openssl-dev && \
    pip install --upgrade pip && \
    pip install -r /src/requirements.txt && \
    cd /src && \
    python manage.py makemigrations && \
    python manage.py migrate

WORKDIR /src