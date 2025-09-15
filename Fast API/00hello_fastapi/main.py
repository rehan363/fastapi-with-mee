from fastapi import FastAPI

app  = FastAPI()

#.get= api methood (GET, POST, PUT, DELETE)
@app.get("/chat")
def hello():
    """this is a hello world function
    agent class"""

    return{"message" : "hello!!!!!"}

@app.post("/chat/start")
def start_chat(messages: dict):
    print("Data received:", messages)
    return messages