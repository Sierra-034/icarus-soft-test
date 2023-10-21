## Instructions to run the project with docker compose
This is similar to the above procedure in terms that we are using a docker container for the database, but in this case we also create a container for our api

### Create images and containers for both, database and api
1. Place on the project root folder which is the same where this README.md file is.
2. Run `docker compose up -d --build`. This will create a container for each both service and is going to start them as well

### Using the api
Here in the root project folder there is a `documentation.yml` file which you can place on a [swagger editor](https://editor.swagger.io/) where you can replace the code or simply upload the `documentation.yml` file.

Or you can simply test the api with the commands in `curl.sh` file placed in this directory.