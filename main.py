from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from typing import Optional
import uvicorn
from router import blog_get, blog_post, user
from db import models
from db.database import engine

app = FastAPI() #instance
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

class Blog(BaseModel):
    title: str #field1
    body: str #field2
    published: Optional[bool] #field3

@app.get('/') #decorate
def index():
    return 'Hey'

@app.get('/about') #decorate
def about():
    print("zaza")
    return {'data' : 'about page'}


@app.get(
        path='/test/{id}', 
        status_code=status.HTTP_200_OK, 
        tags=['test'], 
        summary="Ded test"
        )
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}


models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=9000)

