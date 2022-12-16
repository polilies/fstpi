from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from Blog import schemas

app = FastAPI()

@app.get("/blog")
def index(limit: int, published: bool=True, sort: Optional[str]=None):
    #main path
    if published:
        return {'data': f"{limit} published blog list"}
    else:
        return {'data': "no published blog list"}
    

@app.get('/blog/unpublished')
    #static routing must be before the dynamic routing
def unpublished():
    return {'data':'all unpublished blogs'}
    
@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

class queries(BaseModel):
    id: Optional[int]
    limit: Optional[int]
    on_off: Optional[bool]=False 

@app.get('/blog/{id}/comments')
def comments(id:int, limit: Optional[int], on_off:bool=False):
    #fetch sub comments
    if on_off:
        return {'id': id, "limit": limit}
    else:
        return "Please turn on the lights"

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    


@app.post("/blog")
def create_blog(request: schemas.Device):
    return {"data": f"device is created as the name {request.name} and with the address {request.mod_id}"}