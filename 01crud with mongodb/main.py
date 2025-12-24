from fastapi import FastAPI
from routes.routes import route

app = FastAPI()

app.include_router(route)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Todo API"}
