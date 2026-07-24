from app.database import engine, Base
from app.models.user import User
print("Creating tables.")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")