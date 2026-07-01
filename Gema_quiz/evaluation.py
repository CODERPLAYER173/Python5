from data import category_input, question_number
import matplotlib.pyplot as plt
import pandas as pd
#saves key info like time and score in Missing ,runs in main alongside  save function

def Save_progress(b,time_taken):

    new_row = [[question_number, category_input, time_taken, b]]

    df  = pd.DataFrame(new_row,columns=["Number_Of_Question ", "Category", "Time Taken", "Score"])
    df.to_csv("High_Score.csv",mode='a',index=False,header=False)


