# VARIABLES
ARG image=python:3.9.1-slim-buster

###########
# BUILDER #
###########

# pull official base image
FROM ${image} AS builder

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y python-pip python-dev build-essential

# install git
RUN apt-get update -y && \
    apt-get install -y git

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM ${image}

# set working directory
WORKDIR /usr/src/app

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*
RUN apt-get update -y && \
    apt-get -y install software-properties-common

RUN apt-get update -y && \ 
    apt-get -y install netcat

# install webriver
RUN apt-get update -y && \ 
    apt-get install -y firefox-esr
RUN apt-get install -y wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz
RUN tar -x geckodriver -zf geckodriver-v0.29.0-linux64.tar.gz -O > /usr/bin/geckodriver
RUN chmod +x /usr/bin/geckodriver
RUN rm geckodriver-v0.29.0-linux64.tar.gz

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
