from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_epics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Epic).offset(skip).limit(limit).all()


def get_epic(db: Session, epic_id: int):
    return db.query(models.Epic).filter(models.Epic.id == epic_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_uss(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserStory)\
        .order_by(models.UserStory.id)\
        .offset(skip)\
        .limit(limit).all()


def get_us(db: Session, us_id: int):
    return db.query(models.UserStory).filter(models.UserStory.id == us_id).first()


def update_us_subject(db: Session, db_us: models.UserStory, subject: str, version: int):
    db_us.subject = subject
    db.commit()
    return db_us
