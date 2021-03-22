import os, sys, json
from starlette.responses import JSONResponse
from sqlalchemy.orm.exc import StaleDataError
from fastapi import FastAPI
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app.routers.api import api_router
from app import notifier, Notifier

app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await notifier.generator.asend(None)


@app.exception_handler(StaleDataError)
async def validation_exception_handler(request, exc):
    print(str(exc))

    await notifier.push("Back event " + json.dumps(
            {
                "event": "exception",
                "details": {
                    "code": "OCC.StaleDataError",
                    "text": "Content has been update by another user",
                    "message": str(exc),
                }
            }
        ))

    return JSONResponse(_get_error("StaleDataError", "Content has been update by another user"), status_code=400)


def _get_error(code: str, message: str):
    return {
        "error": {
            "code": code,
            "message": message,
        }
    }
