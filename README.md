### API-Queues-Test

Implementation of FastAPI to send tasks to a Celery-based message queue, using RabbitMQ as a broker and Redis for a
persistent backend.

#### Project Structure:

    . /api-queues-test
    ├── /app              
    |   ├── /celery-remote-worker   
    |   |   ├── __init__.py   
    |   |   ├── Dockerfile
    |   |   ├── requirements.txt
    |   |   └── remote_worker.py
    |   └── /fast-api-implementation   
    |       ├── __init__.py
    |       ├── Dockerfile
    |       ├── requirements.txt
    |       ├── api_endpoints.py
    |       ├── api_worker.py
    |       ├── database.py
    |       ├── fastapi_base.py
    |       └── test.py  
    ├── README.md
    ├── docker-compose.yml
    ├── config.env
    ├── db_config.env
    └── .gitignore

#### Setup:

Build/start all containers with ```docker-compose up -d``` (-d flag runs containers in background).

This will start the API and remote worker, as well as support containers including MSSQL Database, RabbitMQ broker and 
Redis backend.

Stop containers with ```docker-compose down```.

#### Environment Variables:

Envs are stored in config.env and db_config.env (included in .gitignore) and imported by docker-compose.yml. If changing
the default MSSQL password, be sure to change it in each config file.

##### Setup MSSQL Database:

Enter bash shell in DB container with: ```docker exec -it api-queues-test_database_1 bash```.

Login to sqlcmd with: ```/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P $SA_PASSWORD```.

Create the database with: ```CREATE DATABASE {$DB_NAME}```, and execute with ```GO```.

Select the new database and create the table with: ```USE {$DB_NAME}``` 
and ```CREATE TABLE {$DB_TABLE} (item_id int, duration int)```. Execute with ```GO```.

The database is now ready for use.

#### Calling the REST API:

Use your method of choice to access the following endpoints:

    GET  localhost:8000/                (Root endpoint, lists available)
    POST localhost:8000/tasks/receive   (Receive new task, add to DB and Celery Queue, execute task)
    GET  localhost:8000/tasks/status    (Check task status by task_id)

The /tasks/receive endpoint takes a JSON object in the request body of the form:
    
    {
        "item_id": int
        "duration": int
    }

#### Future Implementation Notes:
* Address failures in calculation, use try/excepts and calculation timeout/retry limits?
* Autoscale remote workers as queue size increases
* Authentication for API POST methods
* Move default DB setup to Dockerfile?
* DB filtering for used item_id's
* Expand DB for use as message queue backend?