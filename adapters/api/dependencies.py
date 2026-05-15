from fastapi import Depends
from sqlalchemy.orm import Session

from adapters.repositories.sqlite_car_repository import SQLiteCarRepository
from infrastructure.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_car_repository(db: Session = Depends(get_db)) -> SQLiteCarRepository:
    return SQLiteCarRepository(db)
