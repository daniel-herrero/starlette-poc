from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_userstories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserStory)\
        .order_by(desc(models.UserStory.id))\
        .offset(skip)\
        .limit(limit).all()


def get_us(db: Session, us_id: int):
    return db.query(models.UserStory).filter(models.UserStory.id == us_id).first()


def update_us_subject(db: Session, db_us: models.UserStory, subject: str, version: int):
    db_us.subject = subject
    db_us.version += 1
    db.commit()
    db.refresh(db_us)
    return db_us