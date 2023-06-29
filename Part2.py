from pydantic import BaseModel
from fastapi import Form

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
print(templates)
@app.get("/hello/", response_class=HTMLResponse)
async def hello(request: Request):
   return templates.TemplateResponse("hello.html", {"request": request})


#The jinja2 code elements are put inside the curly brackets.

'''
{% %} – Statements

{{ }} – Expressions to print to the template output

{# #} − Comments which are not included in the template output

# # # − Line statements

'''
@app.get("/home/{name}", response_class=HTMLResponse)
async def home(request: Request, name:str):
   return templates.TemplateResponse("home.html", {"request": request, "name":name, 'ids': [1,2,3,4]})


# Static files
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
@app.get("/employees", response_class=HTMLResponse)
async def employees(request: Request):
   employees = ["Ahmmed", "Mohammed","Ali"]
   return templates.TemplateResponse("employees.html", {"request": request, "employees":employees})


#Forms
#Login form
@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("login.html", {"request": request})


class User(BaseModel):
   username:str
   password:str

@app.post("/submit/", response_model=User)
async def submit(nm: str = Form(...), pwd: str = Form(...)):
   return User(username=nm, password=pwd)