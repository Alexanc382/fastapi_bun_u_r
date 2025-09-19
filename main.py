import os
from fastapi import FastAPI
from starlette.responses import HTMLResponse
import requests
from io import  BytesIO
import questions as que

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():  # функция. которая возвращает в браузер html-страницу
    index_file = os.path.join("static", "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
        return HTMLResponse(content)
