FROM python:3.11-slim AS base

WORKDIR /app

FROM base AS dev

COPY requirements-dev.txt requirements.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

FROM base AS prod

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
