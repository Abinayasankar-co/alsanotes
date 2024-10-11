from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Data(BaseModel):
    input: str


@app.get("/v1/health")
def app_health():
    return {"Alsa":'AlsaNotes is Healthy'}

@app.post("/endpoint")
async def receive_data(data: Data):
    # Process the data as needed
    return {"message": f"Received input: {data.input}"}
