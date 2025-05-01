from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# ---------- User Schemas ----------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    student_id: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    student_id: Optional[str] = None
    is_admin: bool

    class Config:
        from_attributes = True


# ---------- Token Schemas ----------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None


# ---------- Event Schemas ----------

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    date: datetime

class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    location: Optional[str]
    date: datetime
    created_by: int
    qr_code_path: Optional[str] = None

    class Config:
        from_attributes = True


# ---------- Registration Schemas ----------

class RegistrationCreate(BaseModel):
    event_id: int

class RegistrationResponse(BaseModel):
    id: int
    event_id: int
    user_id: int
    checked_in: bool
    qr_data: str

    class Config:
        from_attributes = True
