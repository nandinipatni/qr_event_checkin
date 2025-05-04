# 🎟️ QR Event Check-in System

A backend system for managing college event check-ins using QR codes — built with **FastAPI** and **PostgreSQL**. Built for GDG on Campus SRM Recruitments 2025, this project allows event registration, QR-based attendance, and admin controls.

---

## 🚀 Features

- ✅ JWT-based user authentication (Student & Admin roles)
- 🎫 Event registration with unique QR code generation
- ✉️ QR and event details sent via email
- 📋 Admin dashboard: View attendees, check-in status, and export data
- 📦 PostgreSQL database support
- 🔐 Secure with hashed passwords and token-based routes

---

## 📸 Screenshots

> See `screenshots/` folder in the repo for UI and API examples.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Auth:** JWT (via `python-jose`)
- **Email:** SendGrid
- **QR Generation:** `qrcode` Python library

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/nandinipatni/qr_event_checkin.git
cd qr_event_checkin
```
2. Create Virtual Environment
```bash

Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
```
3. Install Dependencies
```bash
bash
Copy
Edit
pip install -r requirements.txt

```
4. Configure .env
```bash
Create a .env file based on .env.example:

bash
Copy
Edit
cp .env.example .env
Fill in:

env
Copy
Edit
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
5. Run Migrations
```bash
If using Alembic or SQLAlchemy:

bash
Copy
Edit
alembic upgrade head  # Optional if you've setup migrations
```
6. Start the Server
```bash
bash
Copy
Edit
uvicorn app.main:app --reload
Go to: http://127.0.0.1:8000/docs
