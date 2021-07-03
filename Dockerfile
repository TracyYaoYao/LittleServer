FROM python:alpine

COPY . /src

RUN pip install -r /src/requirements.txt && \
    cd /src && \
    python manage.py makemigrations && \
    python manage.py migrate

WORKDIR /src