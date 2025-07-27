FROM python:3.13
RUN adduser --disabled-password timebot
USER timebot
WORKDIR /app
COPY python/requirements.txt .
RUN --mount=type=bind,source=python/ pip install --requirement requirements.txt
