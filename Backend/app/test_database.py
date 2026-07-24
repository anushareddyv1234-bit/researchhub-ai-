from app.database import engine
try:
    connection = engine.connect()
    print("✅ SQLAlchemy connected successfully!")
    connection.close()
except Exception as e:
    print("❌ Connection failed")
    print(e)