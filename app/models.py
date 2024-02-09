from sqlalchemy import Boolean, Integer, Column, ForeignKey, String
from connect import Base

class Todo(Base):
    __tablename__="todo"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    task = Column(String(255))
    is_completed = Column(Boolean, default=False)

class User(Base):
    __tablename__ ="user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))