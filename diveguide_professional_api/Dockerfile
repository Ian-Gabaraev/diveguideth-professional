FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DOCKERIZED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
COPY config/nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
