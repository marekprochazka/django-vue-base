FROM python:3.10-slim-buster AS base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on


ENV WATCHMAN_VERSION=v2022.02.14.00 \ 
    NODE_JS_VERSION=16 \
    NPM_VERSION=8.5.5

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
  apt-get update && apt-get install wget gnupg2 curl -y && \
  echo "deb https://deb.nodesource.com/node_${NODE_JS_VERSION}.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs=$(apt-cache show nodejs|grep Version|grep nodesource|cut -c 10-) yarn && \
  apt-mark hold nodejs && \
  pip install -U pip  && \
  npm i -g npm@^${NPM_VERSION}


# ENTRYPOINT ["entrypoint"]

RUN adduser --disabled-password --gecos "" django

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
  apt update && apt install -y \
  build-essential \
  # Git dependencies
  git openssh-client expect \
  # lxml
  libxml2-dev libxslt-dev \
  # pyodbc
  unixodbc-dev \
  gettext \
  gnupg \
  rsync \
  netcat \
  unzip \
  nano \
  gcc\
  cron \
  rsyslog \
  libcups2-dev\
  python3-dev\
  # php
  apt-transport-https lsb-release ca-certificates


  # https://www.postgresql.org/download/linux/debian/
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt update \
    && apt install -y postgresql-client-13 libpq-dev

# Watchman for Django runserver efficiency https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver
RUN wget https://github.com/facebook/watchman/releases/download/${WATCHMAN_VERSION}/watchman-${WATCHMAN_VERSION}-linux.zip -O /watchman.zip \
    && unzip watchman.zip \
    && mkdir -p /usr/local/{bin,lib} /usr/local/var/run/watchman \
    && cp /watchman-*-linux/bin/* /usr/local/bin \
    && cp /watchman-*-linux/lib/* /usr/local/lib \
    && chmod 755 /usr/local/bin/watchman \
    && chmod 2777 /usr/local/var/run/watchman \
    && rm -rf /watchman-*-linux watchman.zip


COPY ./compose/local/django/bin/start /usr/local/bin/start
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


# Install JS deps
ENV PATH ./services/frontend/node_modules/.bin:$PATH
COPY ./services/frontend/package*.json ./
RUN npm i pm2 -g
RUN npm ci


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


USER django


WORKDIR /app

CMD ["start"]



