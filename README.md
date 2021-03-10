# POC

The same current front-end, served by taiga-front querying two different urls (and services):
* one resolving against the previous Django (taiga-back)
* the other one resolving against the new api POC's urls

## POC Implementation

Currently, the POC enables a PATCH endpoint that allows to update the subject of a user story.

Check the file `src/poc/api2.py`
```python
routes = [
    # ...
    Route("/api2/v1/userstories/{id}", update_us, methods=["PATCH"]),
]
```

Endpoint
`api/v1/userstories/118 (PATCH)`

```json
// From 'US001' to 'US002'
{
  // The new value
  subject: "US002",
  // Consequent updates increase this number by 1
  version: 2
}
```

It remains to be implemented:

* the complete serializing of the user story object, returning linked fields as it's rendered
in taiga-back. Probably using  [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/) if SQLalchemy_serializer 
is not enough.

* finish the rest of calls that taiga's front-end performs when editing the subject of a user story 
(like getting the user story's activity).

* implement the endpoints that taiga's front-end requires for rendering a kanban with a thousand of user stories. 

## POC execution

Please, execute the following commands to execute the POC:
```shell
$ pip3 install -r requirements.txt  # to install the required modules
$ . venv/bin/activate      # loading of python venv
$ python3 src/poc/api2.py  # launching the poc in uvicorn 
```
