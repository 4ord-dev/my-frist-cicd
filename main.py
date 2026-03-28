from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/sub/{a}/{b}")
def sub(a: int, b: int):
    return {"result": a - b}