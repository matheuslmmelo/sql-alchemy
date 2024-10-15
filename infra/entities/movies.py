from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from infra.configs.connection import DBConnectionHandler

class Movies(Base):
    __tablename__ = "movies"

    title = Column(String, primary_key=True)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Movie (title={self.title}, Year={self.year})"        