from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.auth import get_current_user

router = APIRouter(prefix="/register", tags=["Registration"])

@router.post("/{event_id}")
def register_for_event(
    event_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Check if the user is already registered for this event
    existing = db.query(models.Registration).filter_by(user_id=user.id, event_id=event_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already registered")

    # Register the user for the event
    registration = models.Registration(user_id=user.id, event_id=event_id)
    db.add(registration)
    db.commit()
    db.refresh(registration)

    return {"message": "Registered successfully", "event": event.title}
