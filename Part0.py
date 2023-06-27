from fastapi import FastAPI, Path
'''
This app object is the main point of interaction of 
the application with the client browser. 

The uvicorn server uses this object to listen to client’s request.

The next step is to create path operation. 
Path is a URL which when visited by the client invokes visits 
a mapped URL to one of the HTTP methods, 
an associated function is to be executed. 
We need to bind a view function to a URL and the corresponding HTTP method. 
For example, the index() function corresponds to ‘/’ path with ‘get’ operation.
'''
app = FastAPI()

@app.get("/")
async def root():
   return {"message": "Hello World"}
#parameters
#http://127.0.0.1:8000/?name=Mohammed&age=20&city=Hasaka
@app.get('/hello')
async def hello(name:str, age:int, city: str) -> dict:
   return {'name': name,'age': age, 'city': city}

#parameter_validation
#http://127.0.0.1:8000/getname/Mohammed
@app.get("/getname/{name}")
async def getName(name:str=Path(...,min_length=3, max_length=10)):
   return {"name": name}
#http://127.0.0.1:8000/getage/28
@app.get('/getage/{age}')
async def getAge(age:int = Path(...,ge=18,le=100)):
   return {'age': age}
# gt − greater than
# ge − greater than or equal
# lt − less than
# le − less than or equal

#unicorn Part0:app
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/redoc