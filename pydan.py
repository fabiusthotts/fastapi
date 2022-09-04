from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Details(BaseModel):
    name: str
    age: int = None #Write None if the field is not manadatory

@app.post("/postname")
def add_names_post(details: Details, location: str = Body(...)):
    return {"Age": details.age, "Location": location}

if __name__ == "__main__":
    uvicorn.run("pydan:app", reload=True, port=8000)