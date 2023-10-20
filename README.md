## Instructions to run the project on localhost

### Prepare your database container
1. Build a docker image from the `./db/Dockerfile` with `docker build -t icarus/postgres:1.0 -f db/Dockerfile ./db`
2. Run a container from our image: `docker run --name icarus-database-container -p 5432:5432 -e POSTGRES_PASSWORD=somepassword -d icarus/postgres:1.0`
3. To interact with the newly created DB run: `docker exec -it icarus-database-container psql -U postgres`
4. Now type `\c icarus_soft` and you'll connect to *icarus_database* then you can list the tables with `\dt`
4. To quit from the psql client use `\q`

### Create environment variables
Create a file called `.env` in which you'll need to specify the next variables.
```.env
SQLALCHEMY_DATABASE_URI=postgresql://postgres:somepassword@localhost:5432/icarus_soft
```