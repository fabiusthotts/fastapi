from fastapi import FastAPI, Body, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Name(BaseModel):
    name: str

@app.get("/getdata", response_class= HTMLResponse)
def render_page_get(request: Request):
    name = "Fabius"
    return templates.TemplateResponse("index.html", {"request": request, "name": name})

@app.post("/postdata", response_class=HTMLResponse)
def render_page_post(name: str, request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})


if __name__ == "__main__":
    uvicorn.run("htmlres:app", reload=True, port=8000)