FROM python:3.11-slim

RUN apt update && apt install -y gcc libpq-dev

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./ ./

RUN chmod +x run_app.sh
ENTRYPOINT ["/app/run_app.sh"]
