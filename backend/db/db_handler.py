from pymongo import MongoClient
from dotenv import load_dotenv
import bcrypt
import base64
import urllib.parse
from fastapi import HTTPException
import datetime
from PIL import Image
from db.CreatingTokens import create_Token
from io import BytesIO
from fastapi import HTTPException

load_dotenv()

class dbhandles:
    def __init__(self,username="ALSA_LOGIN_MANAGER",password="Abinay@200504") -> None:
        try:
          self.encoded_username = urllib.parse.quote_plus(username)
          self.encoded_password = urllib.parse.quote_plus(password)
          self.Client = MongoClient(f"mongodb+srv://{self.encoded_username}:{self.encoded_password}@alsadocs.2uqmgxl.mongodb.net/?retryWrites=true&w=majority&appName=ALSADOCS")
          self.database = self.Client["ALSA_DB"]
        except Exception as e:
            print(1,e)

    def store_user(self,userid:int,name:str,email:str,password:str,account_type:str,organization :str):
        try:
            self.collections = self.database['ALSA_STORE_USERS']
            hashed_password = self.hash_password(password)
            document = {
               "user_id":userid,
               "name":name,
               "email":email,
               "password":hashed_password,
               "account_type":account_type,
               "Organization": organization,
               "membership": None,
               "active_quizes":[],
               "ack_quizes":[],
               "product":"ALSANotes",
               "tokens":[],
               "created_at":datetime.datetime.now(),
               "updated_at":datetime.datetime.now()
               }
            insert_user = self.collections.insert_one(document)
            if insert_user.acknowledged:
              return {"Success": "The User Account is Succesfully Created", "statuscode": 200}
             
        except Exception as e:
            print(e)
    
    def creating_token(user_id:int,username:str)->str:
        payload = {
            "user_id":user_id,
            "username":username
        }
        token = create_Token(payload)
        if token:
            return token
        else:
            return "NIL"
    
    def login():
        pass

    def forming_quizes(self,quiz_no:int,quiz_creator_name:str,quiz_questions:list,quiz_difficulty:str,quiz_duration:int,quiz_description:str,quiz_members : list, quiz_active_participants: int):
        try:
            self.collections = self.database["ALSA_Quizes"]
            document = {
                "quiz_no": quiz_no,
                "quiz_id": None,
                "quiz_creator_name": quiz_creator_name,
                "quiz_questions": quiz_questions,
                "quiz_difficulty": quiz_difficulty,
                "quiz_duration": quiz_duration,
                "quiz_description":quiz_description,
                "quiz_members": quiz_members,
                "quiz_active_participant": quiz_active_participants,
                "quize_results":[],
                "quize_scores":[],
                "created_at":datetime.datetime.now(),
                "updated_at":datetime.datetime.now(),
            }
            form_quiz = self.collections.insert_one(document)
            if form_quiz.acknowledged:
               return 200
        except  Exception as e:
            print(e)
            return HTTPException(status_code=400,detail="Oops! Some Error Caused None Formation of Quizes.")
    

    def storing_user_history(self,keyword_extraction:list,topic:str,user_id:int):
        try:
           self.collectionhistory =  self.database["ALSA_History"]
           document = {
               "user_id": user_id,
               "topic":topic,
               "Keywords":keyword_extraction
           }
           insert_one = self.collectionhistory.insert_one(document)
           if insert_one.acknowledged:
               return 200
           else:
               return 400
        except Exception as e:
            print(e)
            
    
    def get_quiz_partners(self,quiz_no:int)->list:
        try:
            self.collections1 = self.database["ALSA_Quizes"]
            self.collections2 = self.database["ALSA_STORE_USERS"]
            find_quiz = self.collections1.find_one({"quiz_no":quiz_no})
            if find_quiz:
                partners_list = find_quiz["quiz_members"]
                for i in partners_list:
                    self.collections2.update_one(
                        {'name': i},
                        {
                            "$push": {
                                "active_quizes": find_quiz["quiz_no"]
                            }
                        }
                    )
                return partners_list,200
            return "Nil",403
        except Exception as e:
            print
            return HTTPException(status_code=400,detail="Oops! Some Error Caused ")
    
    def ack_storage(self,name:str,quiz_no:int):
        try:
          self.collections = self.database["ALSA_STORE_USERS"]
          self.collections.update_one(
             {'name':name},
             {'$push':{ "ack_quizes" : quiz_no}},
             upsert=True
            )
          return 200
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400,detail="The ack_user storage problem")
    
    def get_quiz_questions(self,quiz_id:int,quiz_creator_name:str):
        try:
            self.collections = self.database["ALSA_Quizes"]
            find_quiz = self.collections.find_one({"quiz_id":quiz_id , 'quiz_creator_name': quiz_creator_name})
            quiz_questions = find_quiz["quiz_questions"]
            return quiz_questions
        except Exception as e:
            print(e) 

    def store_quiz_value_db(self,storage_value:object,quiz_id:int):
        try:
            self.collections = self.database["ALSA_Quizes"]
            self.collections.update_one(
                    {"quiz_id":quiz_id},
                    {'$push': storage_value},
                    upsert=True
                )
        except Exception as e:
            print(e)
    
    def view_quizes(self,name):
        result = [
         {
           '$match': {
               'name': name
            }
         }
        ]
        for document in result:
           print(document["active_quizes"])

    def hash_password(self,password: str) -> str:
        try:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return hashed.decode('utf-8')
        except Exception as e:
            return {"Error":f"While Processing Request :{e}"}
        
    def check_password(self,password: str, hashed: str) -> bool:
        try : return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except Exception as e: return {"Error":f"While Processing Request:{e}"} 

    def imagetobase64(self,image_path : str):
        with open(image_path, 'rb') as img_file:
           base64_str = base64.b64encode(img_file.read()).decode('utf-8')
        return base64_str

    def display_image(self,user_id:str):
        try:
         image_data = self.collections.find_one({"user_id":user_id})
         if image_data:
             encoded_image =  image_data["image"]
         decoded_img = base64.b64decode(encoded_image)
         return self.convert_to_image_stream(decoded_img)
        except Exception as e:
            print(e)

    def convert_to_image_stream(self, image_data: bytes) -> BytesIO:
        try:
            # Convert the byte data into an image
            image = Image.open(BytesIO(image_data))
            # Create a byte stream for FastAPI response
            img_stream = BytesIO()
            image.save(img_stream,format="PNG")
            img_stream.seek(0)
            return img_stream
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing image: {e}") 

def main():
    store_user = dbhandles()
    store_user.store_user(1,"Abi","abi@gmail.com","sankar@200504")
    

if __name__ == "__main__":
    main()