from db.db_handler import dbhandles
from fastapi import HTTPException


class QuizFormation:
    def __init__(self)->None:
        self.quizinfo = dbhandles()

    def create_quiz(self, quiz_no:int, quiz_creator_name:str, quiz_questions:list, quiz_difficulty:str, quiz_duration:int, quiz_description:str, quiz_members:list , quiz_active_participants:int):
        creating_quiz = self.quizinfo.forming_quizes( 
            quiz_no=quiz_no,
            quiz_creator_name=quiz_creator_name, 
            quiz_questions=quiz_questions, 
            quiz_difficulty=quiz_difficulty, 
            quiz_duration=quiz_duration, 
            quiz_description=quiz_description,
            quiz_members=quiz_members, 
            quiz_active_participants=quiz_active_participants
            
            )
        if creating_quiz == 200:
            return "Sucees! Quiz have been Created"

    async def acknowledge_partner(self,quiz_id):
        try:
           partners = self.quizinfo.get_quiz_partners(quiz_id=quiz_id)
           if partners:
             return f"Msg to all the Members have been sent for acknowledgement!"
           return partners
        except Exception as e:
            print(e)

    async def partner_ack_quiz(self,ack_value: str,name:str,quiz_id:int)->object:
        try:
         if ack_value == "yes":
            if self.quizinfo.ack_storage(name,quiz_id):
               msg = "Quiz has been activated"
               return msg
            else:
                msg = "Something error Occured"
                return msg
        except:
           return HTTPException(status_code=400,detail="Error Occured will try again")
    
    async def participate_quiz():
       pass

    
