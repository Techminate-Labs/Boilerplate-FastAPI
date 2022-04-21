from fastapi import FastAPI
from apps.models.blog import Blog
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/blog")
async def create(request: Blog):
    return {"message": "Hello World"}