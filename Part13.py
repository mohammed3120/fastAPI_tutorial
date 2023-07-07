# FastAPI - Mounting a Sub-App

from fastapi import FastAPI
app = FastAPI()
@app.get("/app")
def mainindex():
   return {"message": "Hello World from Top level app"}

subapp = FastAPI()
@subapp.get("/sub")
def subindex():
   return {"message": "Hello World from sub app"}

app.mount("/subapp", subapp)