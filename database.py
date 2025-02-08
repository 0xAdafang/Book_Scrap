from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://id:password@localhost:5432/database_name" #mettre votre id, password et nom de bdd

engine = create_engine(DATABASE_URL, client_encoding="utf8")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
