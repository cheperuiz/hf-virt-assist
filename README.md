# HF Virtual Assistant

## Sample project

This is a simple template project to store and retrieve very simple models (quotes) in a Mongo database.

## Getting Started

On startup, the script `src/scripts/start_all.sh` starts 2 services:

    1) The <quotes> flask app.
        1.1) The API is exposed on `localhost:5000/hf`. This can be configured in the `factories` module.
        1.2) OpenAPI (Swagger) playgrownd is available on `localhost:5000`.

    2) A Jupyter notebook.
        2.1) You access the notebooks on `localhost:8888`
        2.2) The password is `Iamahacker` but you can change it using the notebook provided.

Additionally, `mongo` and `mongo-express` containers start using the configuration provided in the `.env` file on the root of the project.

### To start the project:

`docker-compose up --build`

Use `Ctrl-C` to stop (twice to kill if it's taking a long time to stop).

`docker-compose down` will remove all containers and networks.

## A quick note about security:

    - Running a misconfigured Jupyter instance in production can be a HUGE security vulnerability, so please don't do it.
    - Be careful on what ports you are actually exposing for public access and make sure those are the only ones punched in the firewall.
