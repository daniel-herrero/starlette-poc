from fastapi import APIRouter
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app import serializers
from app.crud.crud_project import project_crud
from app.core.database import engine, get_db, Base
from starlette.exceptions import HTTPException

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[serializers.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = project_crud.get_multi(db, skip=skip, limit=limit)
    return projects


@router.get("/{project_id}", response_model=serializers.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = project_crud.get(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project
