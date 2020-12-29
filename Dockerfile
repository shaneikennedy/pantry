FROM python:3.8-slim-buster

WORKDIR app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY manage.py scripts/run_web.sh ./
COPY pantry pantry

RUN python manage.py collectstatic --noinput

RUN rm -rf requirements.txt

CMD ["./run_web.sh"]
