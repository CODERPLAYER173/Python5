try :
    question_number = int(input("please enter the number of questions max input - 20 "))
except ValueError:
    print("\nplease enter a number next time")
    quit()
if question_number >= 21:
    print("please enter a number between 1 and 20")
    question_number = int(input("please enter the number of questions max input - 20     "))
category_input = input("""What category would you like to quiz?
    1.Generalknowledge
    2.Sports
    3.History
    4.Science
    5.Geography 
    6.Videogames    
    7.Computers
    8.Evaluate(evaluate your previous progress)
    You Can type the question or you can write the index number        
""").title()
Id = 0
if category_input ==  "Generalknowledge" or category_input == "1":
    Id = 9
elif category_input == "Sports" or category_input == "2":
    Id = 21
elif category_input == "History"  or category_input == "3":
    Id = 23
elif category_input == "Science" or category_input == "4":
    Id = 17
elif category_input == "Geography" or category_input == "5":
    Id = 22
elif category_input == "VideoGames" or category_input == "6":
    Id =15
elif category_input == "Computers" or category_input == "7":
    Id =18
else:
    print("please check your input for spelling and index mistakes")
    quit()




import requests
request = requests.get(f"https://opentdb.com/api.php?amount={question_number}&category={Id}&type=boolean")
data = request.json()
question_data = []
try:
    for x in range(question_number):
        question_data.append(data["results"][x])
except IndexError:
    print("please enter a number lower next time")
