from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

print("Starting database test...")

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL:", DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        print("✅ Database connected successfully!")

except Exception as e:
    print("❌ Database connection failed!")
    print(e)