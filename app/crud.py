from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from app.models import User, Post
from app.schemas import Usuario_Creado, PostCreate

# CRUD para User
async def create_user(db: AsyncSession, user_create: Usuario_Creado, usuario_creado=None):
    db_user = User(**usuario_creado.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


def get_user_by_email():
    return None