FROM python:3.8

RUN pip3 install pipenv

WORKDIR /tmp

COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock

RUN pipenv install --system
