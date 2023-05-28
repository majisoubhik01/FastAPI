from fastapi import APIRouter, status, Response, Query, Path #import
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)
class Blog(BaseModel):
    title: str #field1
    body: str #field2
    published: Optional[bool] #field3
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1':'val1'}

@router.post(
        '/{id}'
        )
def create_blog(request: Blog, id: int, version: int=1):
    return {'data': f'The blog is created with {request.title} with id {id} and version {version}'} # blog and request are the same

@router.post(
    '/new/{id}/comment/{comment_id}'
    )
def create_comment(blog: Blog, id: int,
                    comment_title: int = Query(None,
                                title='Title of the comment',
                                description='Some description of comment_title',
                                alias='commentTitle',
                                deprecated=True
                    ),
                    content: str = Body(...,
                                min_length=10,
                                max_length=50,
                                regex='^[a-z\s]*$'
                    ),
                    v: Optional[List[str]]=Query(None),
                    comment_id: int = Path(ge=5, lt=10)
                ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }