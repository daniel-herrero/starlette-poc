from pydantic import BaseModel


# Shared properties
from pydantic.schema import Optional


class AttachmentBase(BaseModel):
    object_id: Optional[int]
    name: str


# Properties to receive on task creation
class AttachmentCreate(AttachmentBase):
    attached_file: str


# Properties to receive on task update
class AttachmentUpdate(AttachmentBase):
    pass


# Properties shared by models stored in DB
class AttachmentInDBBase(AttachmentBase):
    id: int

    attached_file: str

    class Config:
        orm_mode = True


# Properties to return to client
class Attachment(AttachmentInDBBase):
    pass


# Properties properties stored in DB
class AttachmentInDB(AttachmentInDBBase):
    pass
