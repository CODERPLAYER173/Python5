import time
from quiz_brain import QuizBrain
from evaluation import Save_progress
question_bank = []
def start():
    from question_model import Question

    import data



    global question_bank
    for question in data.question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    print("\n"*20)
start()




quiz = QuizBrain(question_bank)
start_time = time.perf_counter()
while quiz.still_has_questions():
    quiz.next_question()



end_time = time.perf_counter()

time_taken = end_time - start_time

if time_taken > 60:
    time_seconds = time_taken % 60
    time_minutes = int(time_taken // 60)
    time_taken = f'{time_minutes}:{time_seconds:.0f}'
b = quiz.score
print(f"You've completed the quiz in {time_taken} seconds")
print(f"Your final score was: {b}/{quiz.question_number}")

def save():
    with open("quiz_data.csv", "r") as file:
        a = file.read()
        a = int(a)
    if quiz.score >  a:
        with open("quiz_data.csv", "w") as csvfile:
            csvfile.write(f'{quiz.score}')
    Save_progress()

save()