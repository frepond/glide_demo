FROM python:3-alpine

WORKDIR /app

COPY ./accounts_service accounts_service
COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    pip install --no-cache-dir gunicorn && \
    PYTHONPATH=. python accounts_service/manage.py init

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000", "accounts_service.wsgi:app" ]
