class QuizBrain:

    def __init__(self,q_list):
     self.question_number = 0
     self.score = 0
     self.question_list = q_list
    def next_question(self):

        text = self.question_list[self.question_number]
        qna  =  input(f"Q.{self.question_number+ 1} {text.text} (True/False)").lower()
        self.question_number += 1
        self.check_answers(q=qna, ans=text.answer)
    def still_has_questions(self):
      if self.question_number < len(self.question_list):
          return True
      return False
    def check_answers(self,q, ans):
        if q.lower() == ans.lower():
             self.score += 1
             print("You got it right")
        else:
             print("That's wrong")

        print("The answer was",ans)
        print("your score is",self.score,"/",self.question_number)



