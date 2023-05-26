FROM python:3.11-slim

RUN apt update && apt install -y gcc libpq-dev

WORKDIR /app/backend

COPY backend/requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ../ /app

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]
