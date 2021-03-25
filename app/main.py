import os, sys
import logging

from pydantic.error_wrappers import ErrorWrapper, ValidationError
from starlette.responses import JSONResponse, PlainTextResponse
from sqlalchemy.orm.exc import StaleDataError
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app.api.api_router import api_router
from app.api.common_responses import error_response, exception_notification
from app import notifier


app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    logger.setLevel(logging.DEBUG)
    # Prime the push notification generator
    await notifier.generator.asend(None)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_wrapper: ErrorWrapper = exc.raw_errors[0]
    validation_error: ValidationError = error_wrapper.exc
    overwritten_errors = validation_error.errors()
    return JSONResponse(error_response("input.validation.error", "Invalid input parameters", overwritten_errors),
                        status_code=400)


@app.exception_handler(StaleDataError)
async def validation_exception_handler(request, exc):
    logger.warning(str(exc))
    await notifier.push(exception_notification(exc))
    return JSONResponse(error_response("update.staleData.error", "Content has been update by another user"),
                        status_code=400)







