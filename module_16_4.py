from fastapi import FastAPI, Path, HTTPException
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5, max_length=100, example='Vasya', description="Enter username")
    age: int = Field(..., ge=18, le=120, example=25, description="Enter age")

# Инициализируем список пользователей
users: List[User] = [
    User(id=1, username="Arhimandrit", age=100),
]

@app.post('/user/{username}/{age}', response_model=User)
async def add_user(username:str, age:int):
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.get('/users', response_model=List[User])
def show_users():
    return users



@app.put('/user/{user_id}/{username}/{age}', response_model=User)
def update_user(user_id: int, username: str, age:int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            del users[index]
            return {"message": f"The user {user_id} is deleted"}
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.get('/')
def show() -> str:
    return "Все нормально работает! )) продолжай"
