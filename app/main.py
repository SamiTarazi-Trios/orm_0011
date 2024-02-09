from sqlalchemy.orm import Session
import models, crud, schemas
from connect import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()

db = SessionLocal

results = crud.get_user(db, user_id=1)

print(results)