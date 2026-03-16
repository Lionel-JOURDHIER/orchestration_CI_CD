from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Citations(Base):
    __tablename__ = "citations"
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=True)
    author = Column(String, nullable=True)
