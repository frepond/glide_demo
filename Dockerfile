FROM python:3-alpine

WORKDIR /app

ADD ./requirements.txt requirements.txt
ADD ./accounts_service accounts_service

RUN pip install --no-cache-dir -q -r /app/requirements.txt
RUN PYTHONPATH=. python accounts_service/manage.py init

CMD gunicorn --bind 0.0.0.0:$PORT accounts_service.wsgi:app
