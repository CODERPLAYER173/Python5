

def Save_progress():
    import pandas as pd

    from data import category, q_no
    from main import time_taken, b
    new_row = {
        "No_of_questions": q_no,
        "Category": category,
        "time_taken": time_taken,
        "score": b
    }
    a = pd.DataFrame(new_row)
    a.to_csv("Missing questions.csv")
