import os
from fastapi import FastAPI
from livereload import Server
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():  # функция. которая возвращает в браузер html-страницу
    index_file = os.path.join("static", "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
        return HTMLResponse(content)
