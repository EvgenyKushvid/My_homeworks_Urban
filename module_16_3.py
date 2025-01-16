from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
def show_base() -> dict:
    return users


@app.post('/user/{username}/{age}')
def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Vasya")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=25)]
            ) -> dict:
    user_id = str(int(max(map(int, users.keys()), default=0)) + 1)  # Приводим к строке
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} is registered"}


@app.put('/user/{user_id}/{username}/{age}')
def update_user(
        user_id: Annotated[int, Path(ge=0, description="Enter user_id", example=2)],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Vasya")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=25)]
                ) -> dict:
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    users[user_id_str] = f"Имя: {username}, возраст: {age}"
    return {"message": f"The user {user_id} is updated"}


@app.delete('/user/{user_id}')
def delete_user(
        user_id: Annotated[int, Path(ge=0, description="Enter user_id", example=2)]
                ) -> dict:
    user_id_str = str(user_id)
    if user_id_str in users:
        del users[user_id_str]
        return {"message": f"The user {user_id} is deleted"}
    else:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")


@app.get('/')
def show() -> str:
    return "Все нормально! )) продолжай"
