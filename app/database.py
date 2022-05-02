from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------- RAW SQL with PG ------------------------

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fast_api_test', user='postgres', password='', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connecting Successful!")

#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print(error)
#         time.sleep(3)