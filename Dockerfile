FROM python:3.8-slim-buster

WORKDIR pantry

COPY manage.py requirements.txt ./

RUN python -m pip install -r requirements.txt

RUN rm -f requirements.txt

COPY pantry pantry
