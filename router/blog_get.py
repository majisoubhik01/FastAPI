from fastapi import APIRouter, status, Response #import
from pydantic import BaseModel
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get('/') #'id' is dynamic in nature
def comments(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@router.get(
        '/{id}'
        ) #'id' is dynamic in nature
def comments(id:int):
    return {'data': id}


@router.get(
        '/{id}/comments',
        response_description="ID blog"
        ) #'id' is dynamic in nature
def comments(id, g: Optional[int]=10):
    """
    Simulates fetching a comment
    - **id** : Mandatory path parameter
    - **response** : A query parameter
    """
    return {'data': {id:"Yo", 'g':g}}


@router.get(
        '/test2', 
        tags=['test2']
        ) #decorate
def index():
    return 'Hey'