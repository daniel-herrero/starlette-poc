import os, sys, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from typing import List

from fastapi import FastAPI
from starlette.websockets import WebSocket, WebSocketDisconnect
from starlette.responses import JSONResponse
from sqlalchemy.orm.exc import StaleDataError
# from fastapi_poc.sql_app.routers import users
from fastapi_poc.sql_app import crud
from fastapi_poc.sql_app.routers import users, userstories, projects, epics
from fastapi_poc import notifier


app = FastAPI()

app.include_router(users.router)
app.include_router(userstories.router)
app.include_router(projects.router)
app.include_router(epics.router)


@app.get("/push/{message}")
async def push_to_connected_websockets(message: str):
    await notifier.push(f"! Push notification: {message} !")


@app.websocket("/events")
async def websocket_endpoint(websocket: WebSocket):
    await notifier.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Back event (echo) {websocket.client.host}: '{data}'")
    except WebSocketDisconnect:
        notifier.remove(websocket)


@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await notifier.generator.asend(None)


@app.exception_handler(StaleDataError)
async def validation_exception_handler(request, exc):
    print(str(exc))

    await notifier.push(json.dumps(
        {
            "exception": {
                "code": "OCC.StaleDataError",
                "text": "Content has been update by another user",
                "message": str(exc),
            }
        }))

    return JSONResponse(_get_error("StaleDataError", "Content has been update by another user"), status_code=400)


def _get_error(code: str, message: str):
    return {
        "error": {
            "code": code,
            "message": message,
        }
    }
