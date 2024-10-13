from db.db_handler import dbhandles

class QuizFormation:
    def __init__(self)->None:
        self.quizinfo = dbhandles()


    def create_quiz(self, quiz_no, quiz_creator_name, quiz_questions, quiz_difficulty, quiz_duration , quiz_description , quiz_members , quiz_active_participants):
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
        partners = self.quizinfo.get_quiz_partners(quiz_id=quiz_id)
        if partners:
            pass
