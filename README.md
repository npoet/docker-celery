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
    |   |   ├── database.py
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
    ├── .dockerignore
    └── .gitignore

#### Setup:

Start all containers with ```docker-compose up -d```
This will start the API and remote worker, as well as support containers including MSSQL Database, RabbitMQ broker and 
Redis backend.

#### Calling the REST API:

Use Postman, curl etc. to access the following endpoints:

    localhost:8000/                     (Root endpoint, lists available)
    POST localhost:8000/tasks/receive   (Receive new task, add to DB and Celery Queue, execute task)
    GET localhost:8000/tasks/status     (Check task status by task_id)
    GET localhost:8000/tasks/from_db    (Push all DB entries to Celery Queue and execute)
    

#### Future Implementation Notes:
* Address failures in calculation, use try/excepts and calculation timeout/retry limits?
* Autoscale remote workers as queue size increases
* Authentication for API POST methods
* Better code compartmentalization to fit 12 Factor best practices
* DB filtering for used item_id's