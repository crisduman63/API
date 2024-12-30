import os

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://crisduman:1234@localhost/fastapi")