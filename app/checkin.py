from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.auth import get_current_user

router = APIRouter(prefix="/checkin", tags=["Check-in"])

@router.get("/{event_id}")
def checkin(
    event_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    # Check if event exists
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Find registration for this user and event
    registration = db.query(models.Registration).filter_by(user_id=user.id, event_id=event_id).first()
    if not registration:
        raise HTTPException(status_code=403, detail="User not registered for this event")

    # Check if already checked in
    if registration.checked_in:
        raise HTTPException(status_code=400, detail="Already checked in")

    # Mark as checked in
    registration.checked_in = True
    db.commit()

    return {
        "message": "Check-in successful",
        "event": event.title,
        "user": user.email
    }
