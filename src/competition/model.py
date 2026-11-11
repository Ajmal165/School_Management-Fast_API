
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Competition(Base):
    __tablename__ = "competition"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    prize = Column(Boolean)
    # Foreign key to User
    user_id = Column(Integer,ForeignKey("user.id"))
    # Competition belongs to one User (creator)
    creator = relationship("User",back_populates="competitions")
    # One Competition can have multiple Entries
    entries = relationship("Entry",back_populates="competition")
