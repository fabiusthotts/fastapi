from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/welcome/{name}")
def hello(name: str):
    return {"Message": f"Welcome {name}"}

@app.get("/query")
def hello_with_query(query):
    return {"Query": query}
    
if __name__ == "__main__":
    uvicorn.run("intro:app", reload=True, port=8000)