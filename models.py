from sqlalchemy.orm import relationship
from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from datetime import datetime


class User(db.Model):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True, autoincrement=True)
   created_at = Column(DateTime, default=datetime.utcnow)
   email = Column(String, nullable=False, unique=True)
   nombre = Column(String, nullable=False, unique=True)
   generos_preferidos = Column(String, nullable=False, unique=False)
   peliculas_favoritas = Column(String, nullable=False, unique=False)
   directores_favoritos = Column(String, nullable=False, unique=False)
   messages = relationship("Message", back_populates="user")


class Message(db.Model):
   __tablename__ = "messages"
   id = Column(Integer, primary_key=True, autoincrement=True)
   created_at = Column(DateTime, default=datetime.utcnow)
   content = Column(Text, nullable=False)
   author = Column(String, nullable=False)  # 'user' or 'assistant'
   user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
   user = relationship("User", back_populates="messages")
