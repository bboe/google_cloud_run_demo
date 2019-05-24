FROM ubuntu:18.04

WORKDIR /app

RUN apt-get update \
  && apt-get install --no-install-recommends -y python3 python3-pip \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --compile --disable-pip-version-check --no-cache-dir flask gunicorn setuptools

COPY app.py .
CMD exec gunicorn --bind :$PORT --workers 1 --threads 80 app:app
