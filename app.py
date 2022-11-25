from fastapi import FastAPI
from routes.user import user
from routes.vacancy import vacancy
app = FastAPI()

app.include_router(user)
app.include_router(vacancy)



