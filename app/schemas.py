from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class TagBase(BaseModel):
    name: str

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    title: str
    content: str

class Post(PostBase):
    id: int
    tags: List[TagBase]

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class Usuario_Creado(UserBase):
    password: str

class Usuario(UserBase):
    id: int
    posts: List[Post]

    class Config:
        orm_mode = True
class Super_Usuario(UserBase):
    id: int
    password: str
    posts: List[Post]

    class Config:
        orm_mode = True