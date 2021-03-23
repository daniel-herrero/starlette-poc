from fastapi import APIRouter
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import engine, get_db
from app.schemas import schemas
from app.models import models
from app.api import crud
from starlette.exceptions import HTTPException


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task