from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1>{posts[0]["title"]}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts