from db.db_handler import dbhandles
from fastapi import HTTPException

#Used for Quiz Related Aspects
class QuizFormation:
    def __init__(self)->None:
        self.quizinfo = dbhandles()
    
    #used for quiz creation
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
            return "Sucees! Quiz have been Created",200
        else:
           raise HTTPException(status_code=500,detail="Oops Error Occured while creating Quiz")
    
    #Used for Acknowledgment of Quizes
    def acknowledge_partner(self,quiz_id):
        try:
           partners = self.quizinfo.get_quiz_partners(quiz_id=quiz_id)
           if partners:
             return f"Msg to all the Members have been sent for acknowledgement!"
           return partners
        except Exception as e:
            print(e)

    #Used for your Partners Acknowledging the Quiz
    def partner_ack_quiz(self,ack_value: str,name:str,quiz_no:int)->object:
        try:
         if ack_value == "yes":
            if self.quizinfo.ack_storage(name,quiz_no) == 200:
               msg = "Quiz has been activated"
               return msg,200
            else:
                msg = "Something error Occured"
                return msg,400
        except:
           return HTTPException(status_code=400,detail="Error Occured will try again")
    
    #Used for Participating in the Quiz
    def participate_quiz(self,quiz_id:int,quiz_creator_name:str):
        try:
           questions = self.quizinfo.get_quiz_questions(quiz_id,quiz_creator_name)
           return questions         
        except Exception as e:
           print(e)
    
    #Used for Quiz Storages
    def quiz_value_storage(self,name:str,ans_value:list,quiz_id:int):
        try:
           store_ans = {
            "name":name,
            "ans": ans_value
           }
           self.quizinfo.store_quiz_value_db(store_ans,quiz_id)
           
        except Exception as e:
           print(e)
    



