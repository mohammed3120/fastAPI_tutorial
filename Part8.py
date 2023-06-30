'''
Cross-Origin Resource Sharing (CORS) is a situation 

when a frontend application that is running on one 

client browser tries to communicate with a backend 

through JavaScript code, and the backend is in 

a different "origin" than the frontend. 

The origin here is a combination of protocol, 

domain name, and port numbers. 

As a result, http://localhost and https://localhost have different origins.

If the browser with a URL of one origin sends a request for the execution of JavaScript code from another origin, the browser sends an OPTIONS HTTP request.

If the backend authorizes the communication from this different origin by sending the appropriate headers it will let the JavaScript in the frontend send its request to the backend. For that, the backend must have a list of "allowed origins".

'''

# To specify explicitly the allowed origins, 
# import CORSMiddleware and add the list of origins to the app's middleware.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
   "http://192.168.211:8000",
   "http://localhost",
   "http://localhost:8080",
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
@app.get("/")
async def main():
   return {"message": "Hello World"}