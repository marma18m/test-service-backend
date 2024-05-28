# This module will be based on Python 3.10
FROM python:3.10-slim

RUN apt-get update --fix-missing
RUN apt-get install -y git make nano curl wget vim

ENV HOMEDIR=/app
RUN mkdir -p $HOMEDIR

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

WORKDIR $HOMEDIR

ENV PYTHONPATH=$PYTHONPATH:/app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

COPY . $HOMEDIR

RUN poetry config virtualenvs.create false && poetry install 

USER $USERNAME