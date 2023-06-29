import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
app = FastAPI()
class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []
@app.post("/st/")
async def student_data(s1: Student):
   return s1

@app.post("/students/{college}")
async def full_student_data(college:str, age:int, student:Student):
   retval={"college":college, "age":age, **student.dict()}
   return retval

#As it can be seen in Swager page, college is the path parameter, age is a query parameter, and the Student model is the request body.