import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from promptbook.prompt_repo import generate_ppt
from services.PPTGenerator import PowerPointGenerator


app = FastAPI()


class Data(BaseModel):
    input: str

class PPTInput(BaseModel):
    content : list
    categories : list 
    suggestions : str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify the exact origin(s) you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Explicitly allow specific methods
    allow_headers=["*"],  # Allows all headers, you can specify specific headers as well
)

@app.get("/v1/health")
def app_health():
    return {"Alsa":'AlsaNotes is Healthy'}

@app.post("/v1/data_receiver")
async def receive_data(data: Data):
    # Process the data as needed
    return {"message": f"Received input: {data.input}"}


@app.post("/v1/generate_ppt")
async def ppt_generator(ppt : PPTInput):
    try:
      content = ppt.content
      categories = ppt.categories
      suggestions = ppt.suggestions
      prompt = generate_ppt(content,categories,suggestions)
      generator = PowerPointGenerator(json_data=prompt)
      generator.create_presentation()
      return  {"message": "PPT generated successfully"}
    except Exception as e:
        raise HTTPException(status_code=404,detail=f"Oops!Error Occured with status Code  404: {str(e)}")


