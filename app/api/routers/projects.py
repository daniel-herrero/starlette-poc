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
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects


@router.get("/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project