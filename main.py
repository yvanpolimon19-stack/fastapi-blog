from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

posts: list[dict] = [
{
    'id': 1,
    'author': 'CoreyMSchafer',
    'title': 'Blog Post 1',
    'content': 'First post content!',
    'date_posted': 'April 20, 2023'
},
{
    'id': 2,
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content!',
    'date_posted': 'April 21, 2023'
}
]

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
@app.get("/posts",include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
    return posts