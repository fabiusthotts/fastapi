from fastapi import FastAPI, Body, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class= HTMLResponse)
def render_page_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submitdetails", response_class=HTMLResponse)
async def render_page_post(request: Request, username: str = Form(...), details_file: UploadFile = File(...)):
    details = await details_file.read()
    print(details)
    return templates.TemplateResponse("index.html", {"request": request, "name": username})


    
if __name__ == "__main__":
    uvicorn.run("accform:app", reload=True, port=8000)