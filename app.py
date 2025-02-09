from fastapi import FastAPI
from analyze import analyze_sales
from pydantic import BaseModel

app = FastAPI()


class DataModel(BaseModel):
    value: str


@app.post("/summerize")
async def receive_data(data: DataModel):
    print(data)
    res = analyze_sales(data.value)
    return res
