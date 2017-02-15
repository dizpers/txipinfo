FROM ubuntu:latest
MAINTAINER Dmitry Belaventsev <dizpers@gmail.com>

RUN apt-get update -y
RUN apt-get upgrade -y

## Install pre-requisites
RUN apt-get -y install \
#    libffi-dev \
#    libssl-dev \
    python \
    python-dev \
    python-pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD env PYTHONPATH=. twistd -n web --class=server.resource --port=tcp:80