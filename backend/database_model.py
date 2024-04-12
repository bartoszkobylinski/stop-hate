from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class InstagramPost(Base):
    __table__ = "intsagram posts"
    id = Column(Integer, primary_key=True)
    instagram_id = Column(Integer, unique=True, nullable=False)
    name = Column(String)
    media = Column(String)
