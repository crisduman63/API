from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import Post , PostCreate , PostBase
from app.database import get_db  # Asegúrate de que esta función esté definida en tu module de database

router = APIRouter()


class Publicaciones:
    pass

@router.post("/post/", response_model=Publicaciones)
async def create_new_post(
    post: Publicaciones,
    db: Session = Depends(get_db)  # Solo utilizamos get_db
):
    return await Publicaciones(db=db, publicaciones=post)


async def get_post(db, skip, limit):
    pass


@router.get("/post/", response_model=List[Publicaciones])
async def get_post_list(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)  # Mantener esta dependencia también
):
    return await get_post(db=db, skip=skip, limit=limit)