FROM python:alpine

COPY . /src

RUN pip install -r /src/requirement.txt

WORKDIR /src

CMD ["flask", "run", "-h 0.0.0.0 -p 5000"]