from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()

class Country(str, Enum):
    India = "India"
    Canada = "Canada"

countries = {
    'India': ['Kerala','Delhi'],
    'Canada': ['Ontario', 'Alberta'],
}

#Example of enum
@app.get("/get_states/{country}")
def hello(country: Country):
    return {"States": countries.get(country)}

country_id ={
    1: "America",
    2: "Africa",
    3: "India",
}

#Use of type hint, would give a detailed error when given id which is not inetger
@app.get("/get_country/{id}")
def hello_with_query(id: int):
    return {"Country": country_id.get(id)}
    
if __name__ == "__main__":
    uvicorn.run("enum1:app", reload=True, port=8000)