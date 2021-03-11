# POC

Please, execute the following commands to execute the POC:
```shell
$ pip3 install -r requirements.txt.old  # to install the required modules
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

### Websocket

Each time an update database operation is executed, report through a websocket channel `events` notifying with a json 
report that includes the changes

```json
{
    project: 13,
    object {
        obj_type: 'userstory',
        obj_id: 118,
        action: 'update'
    }
}
```

### History of activity

Each time is performed an update database operation, a change report should also be stored in database (Postgres / 
Redis / mongodb).

A simple version about this, could be to store the previous version of the object (with the old values), and the new 
version of the object (including the new values)

With this approach, it should be stored in the database a json serialization of the object, before the change and after:
```json

{
  operation_date: "2021-03-01",
  obj_type: 'userstory',
  old_obj: { 'X json serialization using pydantic?'},
  new_obj: { 'Y json serialization using pydantic?'}
}
```

Ideally, it should be rendered a diff version with updated fields


### Large volume of data

The POC also verified its behaviour when recovering and serializing from database, a large volume of strongly related 
objects.

Mainly, it would be analyzed the process of loading sample data, mapping against tables, and the schemas serialization 
returned in the endpoint.


# Steps to include new packages

Install pip-tools if not installed `$pip install pip-tools`

To include a new package
1. Add the package to requirements.in 
2. Execute `$ pip-compile requirements.in`
3. Install new packages from the generated requirements.txt
`$ pip install -r requirements.txt`

# Good POC references:

https://github.com/tiangolo/full-stack-fastapi-postgresql

https://github.com/Netflix/dispatch

