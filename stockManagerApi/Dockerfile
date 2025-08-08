FROM python:3.13-slim

WORKDIR /usr/local/app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

