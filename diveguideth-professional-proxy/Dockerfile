FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DOCKERIZED=1

WORKDIR /code

COPY requirements.txt /code/
COPY entrypoint.sh /entrypoint.sh
RUN pip install -r requirements.txt

COPY . /code/