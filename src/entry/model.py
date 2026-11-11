
from database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    title = Column(String)
    description = Column(String)
    submission_date = Column(Date)
    # Foreign key to User
    user_id = Column(Integer,ForeignKey("user.id"))
    # Foreign key to Competition
    competition_id = Column(Integer,ForeignKey("competition.id"))
    # Entry belongs to one User
    creator = relationship("User",back_populates="entries")
    # Entry belongs to one Competition
    competition = relationship("Competition",back_populates="entries")
