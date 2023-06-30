# Header Parameters
from typing import Optional
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
app = FastAPI()
@app.get("/headers/")
async def read_header(accept_language: Optional[str] = Header(None)):
   return {"Accept-Language": accept_language} 

@app.get("/rspheader/")
def set_rsp_headers():
   content = {"message": "Hello World"}
   headers = {"X-Web-Framework": "FastAPI", "Content-Language": "ar-SY", "Myname": "Mohammed"}
   return JSONResponse(content=content, headers=headers)