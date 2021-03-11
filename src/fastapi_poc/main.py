from fastapi import FastAPI
from starlette.responses import JSONResponse
from sqlalchemy.orm.exc import StaleDataError
from sql_app.routers import users, userstories

app = FastAPI()

app.include_router(users.router)
app.include_router(userstories.router)


@app.exception_handler(StaleDataError)
async def validation_exception_handler(request, exc):
    print(str(exc))
    return JSONResponse(_get_error("StaleDataError", "Content has been update by another user"), status_code=400)


def _get_error(code: str, message: str):
    return {
        "error": {
            "code": code,
            "message": message,
        }
    }
