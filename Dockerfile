FROM python:alpine

COPY . /src

RUN pip install -r /src/requirement.txt

WORKDIR /src