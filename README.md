# django-vue-base


## Quickstart 
* create `.env` file from `.env.example`
* run docker compose build
* run docker compose up
  * the app is served at port 8000   


## Project description

A 'hacky' solution for SSR vue components that compile entirely into static files.

## Use case
* Define vue components in your frontend folder
* import them into main.ts file
* access them inside django via `BaseVueView`

## Updating dependencies
* run `docker compose run --rm --user root django bash`
* for python run `poetry add ...`
* for frontend go to `services/frontend` and run `npm i ...`


### enjoy

--- 

## Comming soon
* docker.compose.server.yml
* Usage examples


