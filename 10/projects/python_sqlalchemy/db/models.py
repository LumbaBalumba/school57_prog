from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from db import engine

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(engine)
