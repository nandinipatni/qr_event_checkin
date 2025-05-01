from fastapi import FastAPI, HTTPException, Depends
from app import users, events, auth, checkin, register  # ✅ Import all routers
from app.database import engine
from app import models
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.my_utils import generate_qr_code  # Assuming QR generation function is in my_utils.py
from sqlalchemy.orm import Session
from app.database import get_db  # Import the get_db function for dependency injection

# ✅ Create all database tables
models.Base.metadata.create_all(bind=engine)

# ✅ Initialize the FastAPI app
app = FastAPI(
    title="QR Event Check-in System",
    version="1.0.0",
    description="Backend API for event creation, registration, and QR-based check-in"
)

# ✅ Root route
@app.get("/")
def read_root():
    return {"message": "QR Event Check-in system is running 🚀"}

# ✅ Register all routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(events.router)
app.include_router(checkin.router)
app.include_router(register.router)  # ✅ Add the registration route

# ✅ Serve static files for QR codes
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Endpoint to generate and retrieve QR code for event check-in
@app.get("/qr/{event_id}")
async def get_qr(event_id: int):
    """
    Generate and return the QR code image for a specific event.
    
    Args:
    - event_id (int): The ID of the event for which the QR code is being requested.

    Returns:
    - FileResponse: The QR code image as a response.
    """
    # Generate QR code image for the event
    file_path = generate_qr_code(event_id)
    
    # Check if the file exists and return the QR code as a response
    return FileResponse(file_path)

# ✅ New Route to retrieve event details by ID
@app.get("/events/{event_id}")
async def get_event(event_id: int, db: Session = Depends(get_db)):
    """
    Retrieve event details by ID.
    
    Args:
    - event_id (int): The ID of the event to retrieve.
    
    Returns:
    - Event: The event details in JSON format.
    """
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    return event
