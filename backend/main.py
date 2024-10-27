from fastapi import FastAPI,Form,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from promptbook.prompt_repo import generate_ppt
from services.LLm import LLMConfig
from services.PPTGenerator import PowerPointGenerator
from services.RAG import VisualContent
from services.ExtractKeywords import KeywordExtractor


app = FastAPI()


class Data(BaseModel):
    input: str

class PPTInput(BaseModel):
    content : str = Form(...)
    categories : str  = Form(...)
    suggestions : str = Form(...)

class KeywordExtractorInput(BaseModel):
    PdfInput : UploadFile = File(...)

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

@app.post("/v1/create_quiz")
async def create_quiz_main():
    pass

@app.post('/v1/aknowledge_quiz')
async def aknowedge_quiz():
    pass

@app.post('/v1/view_quizes')
async def view_quizes_attended():
    pass

@app.post('/v1/view_quizes_notacknowledged')
async def view_quizes_notacknowledged():
    pass

@app.post('/v1/keyword_extractor')
async def keyword_visibility(user_id:int,KeywordExtract:KeywordExtractorInput)->object:
    try:
        pdffile = KeywordExtract.PdfInput
        visualize = VisualContent(pdf_docs=pdffile)
        content = visualize.chunks
        keywords = KeywordExtractor(language="en-US",context=content,user_id=user_id)
        return  {"user_id":user_id,"TextFile":content,"Keywords":keywords}
    except Exception as e:
        return HTTPException(status_code=404,detail="Oops!We have encountered some Error:")
    
@app.post("/v1/generate_ppt")
async def ppt_generator(ppt : PPTInput):
    try:
      LLM = LLMConfig()
      content = ppt.content
      categories = ppt.categories
      suggestions = ppt.suggestions
      prompt = generate_ppt(content,categories,suggestions)
      result = LLM.llm_request(prompt)
      print(result[0])
      generator = PowerPointGenerator()
      generator.create_presentation(result[0])
      return  {"message": "PPT generated successfully"}
    except Exception as e:
        raise HTTPException(status_code=404,detail=f"Oops!Error Occured with status Code 404: {str(e)}")




