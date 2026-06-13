from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app= FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating:Optional[int]= None

my_posts= [{"title": "title of post 1", "content": "content of post 1", "id":1},
            {"title": "favourite pizza", "content": "I like pizza", "id":2}]


@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/createposts")
def create_posts(post: Post):
    post_dict=post.model_dump()
    post_dict['id'] = randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


