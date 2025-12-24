from fastapi import APIRouter
from models.todo import ToDo
from config.database import collection_name
from bson import ObjectId
from schema.schema import list_serial

route = APIRouter()

@route.get("/get_todos")
async def get_all_todos():
    todos = list_serial(collection_name.find())
    return {"todos": todos}

@route.post("/")
async def create_todo(todo: ToDo):
    collection_name.insert_one(todo.dict())
    return {"message": "Todo created successfully"}

@route.put("/{id}")
async def update_todo(id: str, todo: ToDo):
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": todo.dict()})
    return {"message": "Todo updated successfully"}

@route.delete("/{id}")
async def delete_todo(id: str):
    collection_name.delete_one({"_id": ObjectId(id)})
    return {"message": "Todo deleted successfully"}
