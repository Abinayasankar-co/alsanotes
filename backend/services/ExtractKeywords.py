import yake
from db.db_handler import dbhandles
from fastapi.exceptions import HTTPException

class KeywordExtractor:
    def  __init__(self, language:str,context:list,user_id:str):
      self.language = language
      self.context  = context 
      self.user_id = user_id
      self.kw_extractor = yake.KeywordExtractor()
      self.storevalue = dbhandles()
    
    def extract_context_keywords(self):
      try:
        if len(self.context) == 0:
           raise HTTPException(status_code=400, detail="Context is empty")
        # Extract keywords from the context using YAKE
        kw_list = []
        sw_list  = []

        keywords = self.kw_extractor.extract_keywords(self.context)
        for kw, score in keywords:
          kw_list.append(kw)
          sw_list.append(score)

        n = len(sw_list)

        mid = round(int(n/2))

        keywords_extracted = list(set(kw_list[:mid]))
        storing_db = self.storevalue.storing_user_history(keywords_extracted,self.user_id)
        if storing_db == 200:
           return keywords_extracted
        else:
           return 400
        
      except Exception as e:
         print(e)
         raise HTTPException(status_code=500,detail="Error Occured")
 






