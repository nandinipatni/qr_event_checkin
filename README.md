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

