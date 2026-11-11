from database import Base
from sqlalchemy import Integer, String, Date, Column
from sqlalchemy.orm import relationship
from enum import Enum


class UserType(Enum):
    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    birthdate = Column(Date)
    user_type = Column(String,default=UserType.STUDENT.value,nullable=False)
    # One User can have multiple Entries
    entries = relationship("Entry",back_populates="creator")
    # One User can create multiple Competitions
    competitions = relationship("Competition",back_populates="creator")
