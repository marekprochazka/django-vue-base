# syntax=docker/dockerfile:1
FROM node:lts-alpine as build
WORKDIR /app
COPY ./compose/local/vite/ /usr/local/bin/vite-bin
RUN chmod +x /usr/local/bin/vite-bin/* \
    && find /usr/local/bin/vite-bin/* -type f | xargs sed -i 's/\r$//g' \
    && mv /usr/local/bin/vite-bin/* /usr/local/bin \
    && rmdir /usr/local/bin/vite-bin


# Install JS deps
ENV PATH ./services/frontend/node_modules/.bin:$PATH
COPY ./services/frontend/package*.json ./
RUN npm ci
COPY /compose/local/vite/bin/entrypoint /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]
CMD ["npm","--prefix", "./services/frontend/", "run", "dev"]