# POC execution

Please, execute the following commands to execute the POC:
```shell
$ pip3 install -r requirements.txt  # to install the required modules
$ . venv/bin/activate      # loading of python venv

# Launching uvicorn
cd src/fastapi_poc
$ uvicorn main:app --port 10000 --reload
```
