import fastapi

app = fastapi.FastAPI()

@app.get("/user/admin")
async def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user_by_id(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}

@app.get("/user/{user_name}/{user_age}")
async def read_user_info(user_name: str, user_age: int) -> dict:
    return {"message": f"Информация о пользователе: Имя {user_name}, Возраст {user_age}"}

@app.get("/")
async def first() -> dict:
    return {"message": "Главная страница"}

# python -m uvicorn module_16_1:app