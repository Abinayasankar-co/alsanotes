from fastapi import FastAPI,Form,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional
from promptbook.prompt_repo import generate_ppt,translator
from services.LLm import LLMConfig
from services.PPTGenerator import PowerPointGenerator
from services.RAG import VisualContent
from services.ExtractKeywords import KeywordExtractor
from db.db_handler import dbhandles
from QuizFormer import QuizFormation


app = FastAPI()


class Data(BaseModel):
    input: str

class SignupInput(BaseModel):
    user_id: int = Form(...)
    name :str = Form(...)
    email: str = Form(...)
    password : str = Form(...)
    account_type : str  = Form(...)
    Organization : str  = Form(...)
    membership : Optional[str] =None 

class QuizAcknowledgmentInput(BaseModel):
    ack_value: str = Form(...)
    name:str = Form(...)
    quiz_no:int = Form(...)

class LanguageInput(BaseModel):
    content : str = Form(...)
    language : str =  Form(...)

class PPTInput(BaseModel):
    content : str = Form(...)
    categories : str  = Form(...)
    suggestions : str = Form(...)

class KeywordExtractorInput(BaseModel):
    PdfInput : UploadFile = File(...)

class QuizFormationInput(BaseModel):
        quiz_no:int
        quiz_creator_name:str
        quiz_questions:list 
        quiz_difficulty:str
        quiz_duration:int 
        quiz_description:str
        quiz_members:list
        quiz_active_participants:int

class RequestQuiz(BaseModel):
    quiz_no:int = Form(...)

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

#Signup into ALSANOTES
@app.post("/v1/signup")
async def signup(usersignup : SignupInput):
    try:
      db = dbhandles()
      response = db.store_user(
        userid=usersignup.user_id,
        name=usersignup.name,
        email=usersignup.email,
        password=usersignup.password,
        account_type= usersignup.account_type,
        organization=usersignup.Organization,
      )
      print(response)
      if response["statuscode"] ==  200:
         return response
    except Exception as e:
        raise HTTPException(status_code=404,detail=f'Error Occured{e}')

#Quiz Creation Pipelining
@app.post("/v1/create_quiz")
async def create_quiz_main(quizcreation : QuizFormationInput):
    quizer = QuizFormation()
    result , status_code = quizer.create_quiz(
        quiz_no=quizcreation.quiz_no,
        quiz_creator_name=quizcreation.quiz_creator_name,
        quiz_questions=quizcreation.quiz_questions,
        quiz_difficulty=quizcreation.quiz_difficulty,
        quiz_duration=quizcreation.quiz_duration,
        quiz_description=quizcreation.quiz_description,
        quiz_members=quizcreation.quiz_members,
        quiz_active_participants=quizcreation.quiz_active_participants    
        ) 
    if status_code == 200:
        return {"message":result}

#Accessing Quizes
@app.post("/v1/check_quiz")
async def create_quiz_intel(requestquiz:RequestQuiz):
    try:
     db = dbhandles()
     response,statuscode = db.get_quiz_partners(quiz_no=requestquiz.quiz_no)
     if statuscode == 200:
         return {"message":response}
    except Exception as e:
        raise HTTPException(status_code=404,detail=f'Error Occured{e}')

#Acknowledged Quiz
@app.post('/v1/aknowledge_quiz')
def aknowledge_quiz(quizacknowledgement: QuizAcknowledgmentInput):
    try:
       quizer_ack = QuizFormation()
       result, status_code = quizer_ack.partner_ack_quiz(ack_value=quizacknowledgement.ack_value,
                                                      name=quizacknowledgement.name,
                                                      quiz_no=quizacknowledgement.quiz_no)
       if  status_code == 200:
           return {"message":result}
       else:
           raise Exception
    except Exception as e:
        raise HTTPException(status_code=400,detail="Oops!,Erroor Occured")
    
@app.post('/v1/view_quizes')
async def view_quizes_attended():
    pass

@app.post('/v1/view_quizes_notacknowledged')
async def view_quizes_notacknowledged():
    pass

#Language Conversion Model Request
@app.post("/v1/language_conversion")
async def language_conversion(languageinputs : LanguageInput):
    try:
        lang_converter = LLMConfig()
        prompt = translator(languageinputs.content,languageinputs.language)
        result,status_code = lang_converter.llm_request(prompt)
        if status_code == 200:
            {"Result":result}
        else:
            raise Exception
    except Exception as e:
        raise HTTPException(status_code=403,detail=f"Oops{e}")

#Keyword Extractor Pipielining 
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

#Simpler Powerpoint Generation Pipelining  
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




