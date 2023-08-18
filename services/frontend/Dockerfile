# syntax=docker/dockerfile:1
FROM node:lts-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
RUN npm i
COPY . ./
RUN chmod +x entrypoint
ENTRYPOINT ["/bin/bash", "-c"]