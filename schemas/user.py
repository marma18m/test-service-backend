from fastapi_users.db import SQLModelBaseUser
from fastapi_users import models
from sqlmodel import Field
from typing import Optional


class User(SQLModelBaseUser, table=True):
    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)


class UserCreate(models.CreateUpdateDictModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserUpdate(models.CreateUpdateDictModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserDB(User, models.BaseUserDB):
    pass
