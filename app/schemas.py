from pydantic import BaseModel 

class TodoBase(BaseModel):
    task: str 
    is_completed: bool

class TodoCreate(TodoBase):
    user_id: int

class TodoGet(TodoBase):
    id: int
    user_id: int 

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserGet(UserBase):
    id: int
