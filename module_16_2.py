from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/admin")
async def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user_by_id(user_id:Annotated[int,Path(ge=1, le = 100, description="Enter User id",example=75)]) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}

@app.get("/user/{user_name}/{user_age}")
async def read_user_info(user_name:Annotated[str,Path(min_length=5, max_length=20, description="Enter username", example="Vasya")]
                ,user_age:Annotated[int,Path(ge=18, le = 120, description="Enter age",example=75)]) -> dict:
    return {"message": f"Информация о пользователе: Имя {user_name}, Возраст {user_age}"}

@app.get("/")
async def first() -> dict:
    return {"message": "Главная страница"}

# python -m uvicorn module_16_2:app