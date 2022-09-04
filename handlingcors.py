from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/hello")
async def hello_name():
    return {"Name": "Fabius"}

if __name__ == "__main__":
    uvicorn.run("handlingcors:app", reload=True, port=8000)

