from pymongo import MongoClient
from dotenv import load_dotenv
import bcrypt
import base64
import urllib.parse
import os
import datetime
from PIL import Image
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

    def store_user(self,userid:int,name:str,email:str,password:str,account_type:str,organization :str,imagepath: str):
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
               "image": self.imagetobase64(imagepath),
               "created_at":datetime.datetime.now(),
               "updated_at":datetime.datetime.now(),
               }
            insert_user = self.collections.insert_one(document)
            if insert_user.acknowledged:
              print(f"Success : {insert_user.inserted_id}")
        except Exception as e:
            print(e)


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