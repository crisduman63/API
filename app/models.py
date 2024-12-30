from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base, engine
from app.mixins import SoftDeleteMixin, TimestampMixin

# Tabla intermedia para la relación muchos a muchos (Post-Tag)
post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class User(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    posts = relationship("Post", back_populates="owner")

class Post(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="posts")

    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    posts = relationship("Post", secondary=post_tags, back_populates="tags")

# Modelos Pydantic para las respuestas y solicitudes de la API
class Usuario_Creado(BaseModel):
    name: str
    email: str

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int
    tags: list[int]

class TagCreate(BaseModel):
    name: str




# Crear las tablas en la base de datos
if __name__ == "__main__":
   Base.metadata.create_all(bind=engine)


