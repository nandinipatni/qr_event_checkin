from sqlalchemy.orm import Session
from app import models

def create_event(db: Session, event_name: str, event_date: datetime, event_location: str):
    db_event = models.Event(name=event_name, date=event_date, location=event_location)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
