from cgitb import text
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL
from app.middleware import app

# Configuración de la base de datos asíncrona
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session  = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
SessionLocal =  async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DatabaseConnection:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL)
        self.SessionLocal = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    async def get_session(self) -> AsyncSession:
        async with self.SessionLocal() as session:
            yield session

async def get_db():
    db = DatabaseConnection()
    async for session in db.get_session():
        yield session

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
class SessionLocal:
    pass
# Configura la aplicación FastAPI
app = FastAPI()

async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        statement = text("select 'Hello World'")

        result = await conn.execute(statement)

        print(result)


