from app.database import SessionLocal
from app.models import User
from sqlalchemy.exc import IntegrityError

db = SessionLocal()

admin_user = User(
    name="Admin",
    email="admin@example.com",
    student_id="TISS0001",
    password="admin123",  # Hash this in production!
    is_admin=True
)

try:
    db.add(admin_user)
    db.commit()
    print("Admin user created.")
except IntegrityError:
    db.rollback()
    print("Admin already exists.")
finally:
    db.close()
