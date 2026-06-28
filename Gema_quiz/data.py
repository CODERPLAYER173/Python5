
try :
    question_number = int(input("please enter the number of questions max input - 20 "))
except ValueError:
    print("please enter a number next time")
    quit()
if question_number >= 21:
    print("please enter a number between 1 and 20")
    question_number = int(input("please enter the number of questions max input - 20     "))
category_input = input("""What category would you like to quiz?
    GeneralKnowledge
    Sports
    History
    Science&Nature
    Geography 
    VideoGames    
    Computers         
""").title()
Id = 0
if category_input ==  "GeneralKnowledge":
    Id = 9
elif category_input == "Sports":
    Id = 21
elif category_input == "History":
    Id = 23
elif category_input == "Science&Nature":
    Id = 17
elif category_input == "Geography":
    Id = 22
elif category_input == "Computers":
    Id =18
elif category_input == "VideoGames":
    Id =15

q_no = str(question_number)
category = str(category_input)
import requests




request = requests.get(f"https://opentdb.com/api.php?amount={question_number}&category={Id}&type=boolean")
data = request.json()
question_data = []
try:
    for x in range(question_number):
        question_data.append(data["results"][x])
except IndexError:
    print("please enter a number lower next time")
