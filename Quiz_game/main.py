#only runs when the main file is running not when imported
if __name__ == "__main__":
    import time
    from quiz_brain import QuizBrain
    from evaluation import Save_progress
    question_bank = []
##Functions for start and save
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


    def save(b,time_taken):
        with open("quiz_data.csv", "r") as file:
            a = file.read()
            a = int(a)
        if quiz.score > a:
            with open("Missing_Questions.csv", "w") as csvfile:
                csvfile.write(f'{quiz.score}')
        Save_progress(b,time_taken)
        print("the high score is ",a)




###Start the main code
    start()
    quiz = QuizBrain(question_bank)
    start_time = time.perf_counter()
    while quiz.still_has_questions():
        quiz.next_question()
    end_time = time.perf_counter()
    b = quiz.score

###Quiz Ends

    time_taken = end_time - start_time
    if time_taken > 60:
        time_seconds = time_taken % 60
        time_minutes = int(time_taken // 60)
        time_taken = f'{time_minutes}:{time_seconds:.0f}'
        print(f"You've completed the quiz in {time_taken} ")
        print(f"Your final score was: {b}/{quiz.question_number}")
    elif time_taken < 60:
        time_seconds = round(time_taken,0)
        time_taken = f'{time_seconds:.0f} seconds'
        print(f"You've completed the quiz in {time_taken} ")
        print(f"Your final score was: {b}/{quiz.question_number} and the high score was ")
    save(b,time_taken)
