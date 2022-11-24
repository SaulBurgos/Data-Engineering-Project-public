from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)