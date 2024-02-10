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

#main
def create_user(name : str,email:str):
    db = SessionLocal()
    crud.create_user(db=db,name=name, email=email)
    db.close()
    
def print_users_emails(users):
    # print all the emails of my users 
    for user in users:
        print(user.email)

def remove_user(name :str):
    db = SessionLocal()
    crud.remove_user(db=db,name=name)
    db.close()

print ('-----------------')
todo_users = getUsers()
print_users_emails(todo_users)
print ('-----------------')
remove_user("Anmol")
todo_users = getUsers()
print_users_emails(todo_users)
print ('-----------------')
create_user("Anmol", "anmol@angrypeople.com")

todo_users = getUsers()
print_users_emails(todo_users)


