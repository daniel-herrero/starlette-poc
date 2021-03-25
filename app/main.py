import os, sys, json
from starlette.responses import JSONResponse
from sqlalchemy.orm.exc import StaleDataError
from fastapi import FastAPI

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app.api.api_router import api_router
from app.api.common_responses import error_response, exception_notification
from app import notifier


app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await notifier.generator.asend(None)


@app.exception_handler(StaleDataError)
async def validation_exception_handler(request, exc):
    print(str(exc))

    await notifier.push(exception_notification(exc))

    return JSONResponse(error_response("staleData", "Content has been update by another user"), status_code=400)







