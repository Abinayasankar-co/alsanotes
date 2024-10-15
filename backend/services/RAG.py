from PyPDF2 import PdfReader
from fastapi import HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
import urllib.parse
from dotenv import load_dotenv
from LLm import LLMConfig
from pymongo import MongoClient
import os 

load_dotenv()

class VisualContent:
    def __init__(self,pdf_docs:str) -> None:
       self.encoded_username = urllib.parse.quote_plus('ALSA_LOGIN_MANAGER')
       self.encoded_password = urllib.parse.quote_plus('Abinay@200504')
       self.embed_vector = LLMConfig()
       self.Client = MongoClient(f"mongodb+srv://{self.encoded_username}:{self.encoded_password}@alsadocs.2uqmgxl.mongodb.net/?retryWrites=true&w=majority&appName=ALSADOCS")
       self.collection = self.Client["ALSA_DB"]["ALSA_Vector_col"]
       self.pdf_docs = pdf_docs
       self.text = ""
       self.chunks = []


    
    def get_pdf_text(self):
        try:
            if not self.pdf_docs or self.pdf_docs == ".":
                raise ValueError("Invalid PDF file path provided.")
            with open(self.pdf_docs, "rb") as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                self.text = ""
                for page in pdf_reader.pages:
                    self.text += page.extract_text()
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"PDF file not found at: {self.pdf_docs}")     
        except PermissionError:
            raise HTTPException(status_code=403, detail=f"Permission denied for file: {self.pdf_docs}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

    def get_text_chunks(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        self.chunks = text_splitter.split_text(self.text)  

    def storing_vectors(self,user_id:int,name:str):
        try:  
            embed_list = []
            if not self.chunks:
                raise ValueError("No data available for embedding.")     
            for chunk in self.chunks:
                embedded_text = self.embed_vector.llm_embedding(chunk)
                embed_list.append({"user_id":user_id,"name":name,"chunk": chunk, "embedding": embedded_text})
            if embed_list:
                self.collection.insert_many(embed_list)    
            return {"Db": "Embeddings have been successfully saved"} 
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
    
    def query_results(self,query):
        results = self.collection.aggregate([
                        {
                          "$vectorSearch": {
                          "index": "ALSA_Vectors",
                          "path": "embedding",
                          "queryVector": self.embed_vector.llm_embedding(query),
                          "numCandidates": 50,
                          "limit": 5
                        }
                        }
            ])
        for document in results:
            print(document)

def main():
    try:
      query = " Give only the Objective"
      visualize = VisualContent(pdf_docs="../Output/TestingCopilot.pdf") 
      if query:
        visualize.query_results(query)
      else:
        visualize.get_pdf_text()
        visualize.get_text_chunks()
        result = visualize.storing_vectors()
        print(result)
    except Exception as e:
       raise HTTPException(status_code=404,detail=f"Hello {e}")


if __name__ == '__main__':
    main()
