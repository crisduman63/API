import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base_base = declarative_base()

class Base(Base_base):
    __tablename__ = 'mi_modelo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
print(sys.path)
print(sys.path)