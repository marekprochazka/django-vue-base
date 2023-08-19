FROM python:3.10-slim-buster AS base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN adduser --disabled-password --gecos "" django


COPY ./compose/test/django/bin/start /usr/local/bin/start
RUN chmod +x /usr/local/bin/start \
    && find /usr/local/bin/start -type f | xargs sed -i 's/\r$//g'

# Install Python deps
RUN pip install -U pip \
    && pip install poetry \
    && pip install pyuwsgi==2.0.21 \
    && pip install uwsgitop==0.11 \
    && pip install uwsgi-tools \
    && poetry config virtualenvs.create false


COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-interaction --no-ansi -vvv


#
# DEV
#
FROM base AS dev

ARG UID
ARG GID
ENV UID $UID
ENV GID $GID

RUN usermod -u $UID django \
    && groupmod -g $GID django