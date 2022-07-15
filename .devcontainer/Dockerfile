# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.9
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV PYTHONUNBUFFERED 1

RUN apt-get -qq update && apt-get install -qq -y git curl bash zip && apt-get install -qq -y build-essential

ENV DOCKER_VERSION=20.10.11
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz \
        && tar xzvf docker-${DOCKER_VERSION}.tgz --strip 1 \
        -C /usr/local/bin docker/docker \
        && rm docker-${DOCKER_VERSION}.tgz
        
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

COPY src/requirements.txt ./src/requirements.txt
RUN pip install --user -r src/requirements.txt