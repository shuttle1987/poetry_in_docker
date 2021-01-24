FROM python:3.9-slim
LABEL maintainer="consulting@lesinskis.com"
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1
COPY . /code/

WORKDIR /code/
