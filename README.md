# POC

Please, execute the following commands to execute the POC:
```shell
$ pip3 install -r requirements.txt  # to install the required modules
$ . venv/bin/activate      # loading of python venv

# Launching uvicorn
cd src/fastapi_poc
$ uvicorn main:app --port 10000 --reload
```

## Endpoints

Access the documentation to check the enabled endpoints:

http://127.0.0.1:10000/docs
http://127.0.0.1:10000/redoc

## This POC tries to cover

### Modeling and database operation 

How easy is to connect, model each table's fields, and operate an existing Postgres database. 

### Serializers

How easy is to create the schemas that will expose the intended fields through the different endpoints 

### Optimistic concurrency control

The OCC will be achieved checking the `version` variable on the database before committing the changes. If the version 
values doesn't match, someone has update this db register before.

### Websocket / Webhook

Each time an update database operation is executed, some webhooks or websocket channels should be notified reporting 
about the change

### History of activity

Each time is performed an update database operation, a change report should also be stored in Redis / mongodb.
