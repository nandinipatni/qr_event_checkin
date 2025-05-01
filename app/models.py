from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    student_id = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    registrations = relationship("Registration", back_populates="user")
    events = relationship("Event", back_populates="creator")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    location = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    qr_code_path = Column(String)

    created_by = Column(Integer, ForeignKey("users.id"))
    registrations = relationship("Registration", back_populates="event")
    creator = relationship("User", back_populates="events")

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    checked_in = Column(Boolean, default=False)
    qr_data = Column(String, unique=True)

    user = relationship("User", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")

    __table_args__ = (UniqueConstraint('user_id', 'event_id', name='_user_event_uc'),)
