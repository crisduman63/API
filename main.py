from asyncio.log import logger
from logging import raiseExceptions
from typing import List, Optional, Any, Sequence
from absl.logging import exception
from fastapi import FastAPI, Depends, HTTPException
from psutil import users
from pydantic import BaseModel
from sqlalchemy import Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.testing import db
from starlette.responses import JSONResponse
from app.database import SessionLocal, engine
from app.models import User, Base

app = FastAPI()

# Modelo Pydantic para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    email: str

# Modelo Pydantic para la salida de datos de usuarios
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

# Dependencia para obtener la sesión de la base de datos
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.exception_handler(Exception)
def handle_exception(request, exc):
    logger.error(f"An error occurred: {exc}")
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

@app.get('/')
async def read_root():
    return {"Mensage": "Hello Mundo"}

@app.get('/users/{name}')
async def get_user(name: str):
    user = db()
    if user:
        return {"user": user}
    else:
        return {"error": "User not found"}


# Crear un nuevo usuario
@app.post('/users/')
async def nuevo_usuario(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.username, email=user.email)
    db.add(new_user)
    db.commit()

# Obtener usuarios por nombre de usuario
@app.get('/users/{username}', response_model=List[UserOut])
async def obtener_usuario(username: str, db: AsyncSession = Depends(get_db)) -> Sequence[Row[Any] | RowMapping | Any]:
    result = await db.execute(select(User).where(username == User.username))
    users1 = result.scalars().all()
    try:
      if not users1:
        raise HTTPException(status_code=404, detail="No users found with the specified username")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return users1

# Eliminar un usuario por ID
@app.delete('/users/{user_id}')
async def borrar_usuario(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(user_id == User.id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return {"message": "User deleted successfully"}











