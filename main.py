#          █  █ █▄ █ █▄ █ █▀▀ ▀▄▀ █▀█ █▄ █
#          ▀▄▄▀ █ ▀█ █ ▀█ ██▄  █  █▄█ █ ▀█ ▄
#                © Copyright 2025
#            ✈ https://t.me/unneyon

# 🔒 Licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0
# + attribution
# + non-commercial
# + no-derivatives

# You CANNOT edit, distribute or redistribute and use for any purpose this file without direct permission from the author.
# All source code is provided for review only.

import datetime
import dateutil
import dateutil.relativedelta
import json
import uvicorn
import subprocess

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

config = json.loads(open("config.json", "r", encoding="utf-8").read())


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request
        }
    )

@app.get("/donate")
async def index(request: Request):
    return templates.TemplateResponse(
        name="donate.html",
        context={
            "request": request
        }
    )

@app.get("/projects")
async def index(request: Request):
    return templates.TemplateResponse(
        name="projects.html",
        context={
            "request": request
        }
    )

@app.get("/music")
async def index(request: Request):
    return templates.TemplateResponse(
        name="music.html",
        context={
            "request": request
        }
    )

@app.get("/script.js")
async def index(request: Request):
    return PlainTextResponse(
        content=open(f"static/script.js", "r").read(),
        status_code=200
    )


if __name__ == "__main__":
    print(f"\033[36m          █  █ █▄ █ █▄ █ █▀▀ ▀▄▀ █▀█ █▄ █\033[0m")
    print(f"\033[36m          ▀▄▄▀ █ ▀█ █ ▀█ ██▄  █  █▄█ █ ▀█ ▄\033[0m")
    print(f"\033[36m                © Copyright 2025\033[0m")
    print(f"\033[36m            ✈ https://t.me/unneyon\033[0m", end="\n\n")
    print(f"\033[36m 🔒 Licensed under CC-BY-NC-ND 4.0 unless otherwise specified.\033[0m")
    print(f"\033[36m 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0\033[0m")
    print(f"\033[36m + attribution\033[0m")
    print(f"\033[36m + non-commercial\033[0m")
    print(f"\033[36m + no-derivatives\033[0m", end="\n\n")
    print(f"\033[36m You CANNOT edit, distribute or redistribute and use for any purpose this file without direct permission from the author.\033[0m")
    print(f"\033[36m All source code is provided for review only.\033[0m")
    print(f"\033[36mСайт [BIO] успешно запущен!\033[0m")

    uvicorn.run(app, host="0.0.0.0", port="14028")