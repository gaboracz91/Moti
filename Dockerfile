FROM python:3-alpine

WORKDIR /app

RUN apk add --update postgresql-libs postgresql-dev python3-dev gcc musl-dev

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/dumb-init", "/app/entrypoint.sh"]