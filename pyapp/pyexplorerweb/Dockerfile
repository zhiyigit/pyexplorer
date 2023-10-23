FROM python:3.11-slim

RUN apt-get -y update && \
    apt-get -y install ssh git wget

RUN pip install poetry

RUN mkdir -p /pyapproot

COPY pyapp/pyexplorerweb /pyapproot/pyapp/pyexplorerweb
COPY pyshared /pyapproot/pyshared

COPY pyapp/pyproject.toml /pyapproot/pyapp/pyproject.toml
COPY pyapp/poetry.lock /pyapproot/pyapp/poetry.lock

WORKDIR /pyapproot/pyapp

RUN poetry export -f requirements.txt --without-hashes --output /tmp/requirements.txt

RUN --mount=type=ssh pip install -r /tmp/requirements.txt

WORKDIR /pyapproot/pyapp/pyexplorerweb

ENV PYTHONPATH=/pyapproot:/pyapproot/pyshared

EXPOSE 8090

CMD ["python", "/pyapproot/pyapp/pyexplorerweb/app.py"]
#CMD ["/bin/bash"]