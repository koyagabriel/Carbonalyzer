# Carbonalyzer

## Starting the app.

### Starting the API Server (backend)
1. Start up your terminal.
2. Ensure that you've `docker` installed on your machine.
3. Navigate into the server directory and rename `.evn.example` to `.env`. Predefined values have been assigned to each variable, but you can update them if need be.

             POSTGRES_DB: <the name of your database>
             POSTGRES_PASSWORD: <database password>
             POSTGRES_USER: <database user>
             TOKEN_LIFETIME_IN_MINUTES: <token life span>
             DB_BIND_PORT: <port through which you can access the database in the container from your host machine>
             SERVER_BIND_PORT: <port through which you can access the server in the container from your host machine>
   
4. Navigate back to the root directory.
5. Run command `docker-compose up --build` to spin up the services
6. Visit the route `http://localhost:8000/swagger/` to view the API documentation. 
7. Note that the port in the url is based on the predefined value set in .env. Update the port in the url accordingly if changes were made to `.env`.

### Developer
Koya Adegboyega.