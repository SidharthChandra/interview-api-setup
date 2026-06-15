from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel
from typing import Dict, Optional, Generic, TypeVar

T=TypeVar("T")

app = FastAPI()
db:Dict[int,"User"]=dict()

class User(BaseModel):
   id:int
   user_name:str

class ResponseModel(BaseModel, Generic[T]):
   message:str
   data: Optional[T] = None

@app.get("/user",response_model=ResponseModel[Dict[int,User]])
def get_users():
   return ResponseModel(statuscode=200, message="Users fetched successfully", data=db)


@app.get("/user/{id}",response_model=ResponseModel[User])
def get_user(id:int):
   if id in db:
      return ResponseModel(message="User fetched successfully", data=db.get(id))
   return HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="User not found")

@app.post("/user/",response_model=ResponseModel[User], status_code = status.HTTP_201_CREATED)
def create_user(user:User):
   if user.id in db:
      return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,detail="User already present in db")
   db[user.id]=user
   return ResponseModel(message="User created successfully", data=user)
   

