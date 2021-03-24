from pydantic import BaseModel

from pydantic.schema import datetime, Optional


# Shared properties
class UserBase(BaseModel):
    username: str
    full_name: str
    photo: str
    is_active: bool
    is_superuser: bool
    email: str
    color: str
    bio: str
    date_joined: datetime
    lang: str
    timezone: str
    colorize_tags: bool
    is_system: bool
    theme: str
    uuid: str
    accepted_terms: bool
    read_new_terms: bool
    verified_email: bool
    is_staff: bool

    last_login: Optional[datetime] = None
    token:  Optional[str]
    email_token:  Optional[str]
    new_email:  Optional[str]
    max_private_projects:  Optional[int]
    max_public_projects:  Optional[int]
    max_memberships_private_projec:  Optional[int]
    max_memberships_public_projects:  Optional[int]


# Properties to receive on task creation
class UserCreate(UserBase):
    password: str


# Properties to receive on task update
class UserUpdate(UserBase):
    password: Optional[str]


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class User(UserInDBBase):
    pass


# Properties properties stored in DB
class UserInDB(User):
    pass
