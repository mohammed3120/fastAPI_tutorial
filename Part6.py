# Response Model
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   marks: List[int] = []
   percent_marks: float
class percent(BaseModel):
   id:int
   name :str = Field(None, title="name of student", max_length=10)
   percent_marks: float
@app.post("/marks", response_model=percent)
async def get_percent(s1:student):
   s1.percent_marks=sum(s1.marks)/(len(s1.marks))
   return s1

# nested Models
from typing import Tuple
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class supplier(BaseModel):
   supplierID:int
   supplierName:str
class product(BaseModel):
   productID:int
   prodname:str
   price:int
   supp:supplier
class customer(BaseModel):
   custID:int
   custname:str
   prod:Tuple[product]

@app.post('/invoice')
async def getInvoice(c1:customer):
   return c1