# CRUD Operations (Create, Read, Update, Delete)
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
data = []
class Book(BaseModel):
   id: int
   title: str
   author: str
   publisher: str

# Create
@app.post("/book")
def add_book(book: Book):
   data.append(book.dict())
   return data

# Read
@app.get("/list")
def get_books():
   return data

@app.get("/book/{id}")
def get_book(id: int):
   id = id - 1
   return data[id]

# Update
@app.put("/book/{id}")
def add_book(id: int, book: Book):
   data[id-1] = book
   return data

# Delete
@app.delete("/book/{id}")
def delete_book(id: int):
   data.pop(id-1)
   return data