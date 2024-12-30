from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import Usuario_Creado, Usuario
from app.crud import create_user, get_users
from app.database import get_db  # Asegúrate de que esta función esté definida en tu module de database

router = APIRouter()

@router.post("/users/", response_model=Usuario)
async def create_new_user(
    user: Usuario_Creado,
    db: Session = Depends(get_db)  # Solo utilizamos get_db
):
    return await create_user(db=db, user_create=user)

@router.get("/users/", response_model=List[Usuario])
async def get_users_list(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)  # Mantener esta dependencia también
):
    return await get_users(db=db, skip=skip, limit=limit)