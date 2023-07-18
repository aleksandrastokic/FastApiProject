from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    age:int
    gender: str | None = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello/{name}")
def say_hello_to_someone(name: str):
    return {"message": f"Hello {name}"}

@app.post("/items")
async def create_item(item:Item):
    return item