FROM python:3.11-slim

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
