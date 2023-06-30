from fastapi import FastAPI, Depends, HTTPException
app = FastAPI()
'''
async def dependency(id: str, name: str, age: int):
   return {"id": id, "name": name, "age": age}

@app.get("/user/")
async def user(dep: dict = Depends(dependency)):
   return dep
'''
class Dependency:
   def __init__(self, id: str, name: str, age: int):
      self.id = id
      self.name = name
      self.age = age 

async def validate(dep: Dependency = Depends(Dependency)):
   if dep.age > 18:
      raise HTTPException(status_code=400, detail="You are not eligible")
   else:
      return dep
   
@app.get("/user/", dependencies=[Depends(validate)])
async def user():
   return {'status': 'success'}

@app.get("/admin/")
async def admin(dep: Dependency = Depends(Dependency)):
   return dep 

