from sqlalchemy.orm import Session
import models, crud, schemas
from connect import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
## todo 
## add a function to get user that takes a parameter user id and execute below
def getUser(userId):
    db = SessionLocal()
    user = crud.get_user(db=db, user_id=userId)
    db.close()
    return user

## to do create another function that gets ALL users 
def getUsers():
    db = SessionLocal()
    users = crud.get_users(db)
    db.close
    return users

todo_users = getUsers()
# print all the emails of my users 
for todo_user in todo_users:
    print(todo_user.email)