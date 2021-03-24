from app.crud.Base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDDbUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass


users_crud = CRUDDbUser(User)
