from app.crud.Base import CRUDBase
from app.models.epic import Epic
from app.schemas.epic import EpicCreate, EpicUpdate


class CRUDEpic(CRUDBase[Epic, EpicCreate, EpicUpdate]):
    pass


epic_crud = CRUDEpic(Epic)
