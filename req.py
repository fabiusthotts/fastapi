from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()

names = []

@app.put("/putname/{name}")
def add_names_put(name: str):
    names.append(name)
    return {"List of names": names}

@app.post("/postname")
def add_names_post(name: str):
    names.append(name)
    return {"List of names": names}

@app.put("/deletename/{name}")
def add_names_put(name: str):
    names.remove(name)
    return {"List of names": names}

@app.api_route("/handledata", methods=['GET','POST'])
def handle_data(name: str):
    names.append(name)
    return {"List of names": names}

    
if __name__ == "__main__":
    uvicorn.run("req:app", reload=True, port=8000)