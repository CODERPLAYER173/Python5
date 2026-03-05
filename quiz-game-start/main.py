from  data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank =[]
for i in range(0,10):
    text = question_data[i].get("question")
    answer = question_data[i].get("correct_answer")
    new_q = Question(text=text,answer=answer)
    Question_bank.append(new_q)

Qna = QuizBrain(Question_bank)
while Qna.still_has_questions():
    Qna.next_question()

while not Qna.still_has_questions():
    print("you have completed the quiz ")
    print(f'your final score was {Qna.score}/{Qna.question_number}')
    break