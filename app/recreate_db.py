from database import engine
from models import Base

print("⏳ Dropping all tables...")
models.Base.metadata.drop_all(bind=engine)

print("✅ Creating tables from updated models...")
models.Base.metadata.create_all(bind=engine)

print("🚀 Done: Database schema reset.")
