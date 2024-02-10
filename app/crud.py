import models, schemas
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db:Session):
    return db.query(models.User)

def create_user(db:Session,name : str,email : str):
    new_user = models.User(name=name, email=email)
    db.add(new_user)
    db.commit()

def remove_user(db: Session, name: str):
    user = db.query(models.User).filter(models.User.name == name).first()
    if user:
        db.delete(user)
        db.commit()

