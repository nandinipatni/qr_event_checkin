from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user
from app.qr_utils import generate_qr_code
import uuid

router = APIRouter(prefix="/events", tags=["Events"])

# ✅ Create a new event (admin only)
@router.post("/create")
def create_event(
    event: schemas.EventCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create events")

    db_event = models.Event(**event.dict(), created_by=user.id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    # Generate QR code for the event (optional: could be used for event-level check-in)
    qr_path = generate_qr_code(db_event.id)
    db_event.qr_code_path = qr_path
    db.commit()

    return {
        "message": "Event created successfully",
        "event": {
            "id": db_event.id,
            "title": db_event.title,
            "description": db_event.description,
            "location": db_event.location,
            "date": db_event.date,
            "qr_code_path": db_event.qr_code_path
        }
    }

# ✅ List events created by current user
@router.get("/my-events")
def list_user_events(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    events = db.query(models.Event).filter(models.Event.created_by == user.id).all()
    return events

# ✅ Register current user for an event
@router.post("/{event_id}/register")
def register_for_event(
    event_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    existing = db.query(models.Registration).filter_by(user_id=user.id, event_id=event_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already registered for this event")

    # Generate unique QR data for this registration
    qr_data = str(uuid.uuid4())
    registration = models.Registration(
        user_id=user.id,
        event_id=event_id,
        qr_data=qr_data
    )
    db.add(registration)
    db.commit()
    db.refresh(registration)

    return {
        "message": "Successfully registered for event",
        "event_id": event_id,
        "user_id": user.id,
        "qr_data": qr_data
    }

# ✅ Check-in via QR code
@router.post("/checkin/{qr_data}")
def checkin_via_qr(
    qr_data: str,
    db: Session = Depends(get_db)
):
    registration = db.query(models.Registration).filter_by(qr_data=qr_data).first()
    if not registration:
        raise HTTPException(status_code=404, detail="Invalid or expired QR code")

    if registration.checked_in:
        raise HTTPException(status_code=400, detail="User already checked in")

    registration.checked_in = True
    db.commit()

    return {
        "message": "Check-in successful",
        "user_id": registration.user_id,
        "event_id": registration.event_id
    }
