FROM python:alpine

COPY . /src

RUN pip install -r /src/requirements.txt

WORKDIR /src
