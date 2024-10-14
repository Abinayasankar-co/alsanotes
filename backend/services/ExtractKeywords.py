import yake

class KeywordExtractor:
    def  __init__(self, language:str,context:list):
      self.language = language
      self.context  = context
      self.kw_extractor = yake.KeywordExtractor()
    
    def extract_context_keywords(self):
       # Extract keywords from the context using YAKE
       kw_list = []
       sw_list  = []

       keywords = self.kw_extractor.extract_keywords(self.context)
       for kw, score in keywords:
          kw_list.append(kw)
          sw_list.append(score)

       n = len(sw_list)

       mid = int(n/2)

       keywords_extracted = list(set(kw_list[:mid]))
       
       return keywords_extracted
    
    def storing_keywords_in_report():
       pass
        





