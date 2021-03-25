from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.crud.Base import CRUDBase
from app.db_models.user import User
from app.validators.user import UserCreateVal, UserUpdateVal


class CRUDDbUser(CRUDBase[User, UserCreateVal, UserUpdateVal]):
    @staticmethod
    def get_by_email(db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_username(db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreateVal) -> User:
        db_obj = User(
            password=get_password_hash(obj_in.password),
            username=obj_in.username,
            full_name=obj_in.full_name,
            email=obj_in.email,
            is_superuser=obj_in.is_superuser,
            is_active=obj_in.is_active,
            color=obj_in.color,
            bio=obj_in.bio,
            date_joined=obj_in.date_joined,
            colorize_tags=obj_in.colorize_tags,
            is_system=obj_in.is_system,
            uuid=obj_in.uuid,
            accepted_terms=obj_in.accepted_terms,
            read_new_terms=obj_in.read_new_terms,
            verified_email=obj_in.verified_email,
            is_staff=obj_in.is_staff,
            theme=obj_in.theme,
            photo=obj_in.photo,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


users_crud = CRUDDbUser(User)
