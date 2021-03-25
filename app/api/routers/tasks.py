from fastapi import APIRouter
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app.crud.crud_task import task_crud
from app.core.database import engine, get_db, Base
from app import serializers

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[serializers.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = task_crud.get_multi(db, skip=skip, limit=limit)

    return tasks


@router.get("/{task_id}", response_model=serializers.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_crud.get(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return db_task
