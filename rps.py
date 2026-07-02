import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("rock paper or scissor\n").lower()
if user_input == "rock":
    print(rock)
elif user_input == "paper":
    print(paper)
elif user_input == "scissors":
    print(scissors)
else:
    print("invalid input")
choice = ["rock","paper","scissors"]
computer_input = random.choice(choice)
if computer_input == "rock":
    print(rock)
elif computer_input == "paper":
    print(paper)
elif computer_input == "scissors":
    print(scissors)
else:
    print("Invalid input")
if computer_input == user_input:
    print("tie")
elif computer_input == "rock" and  user_input == "scissors" or computer_input == "scissors" and  user_input == "paper" or computer_input == "paper" and user_input == "rock":
    print("computer wins")
elif user_input  == "rock" and  computer_input == "scissors" or user_input == "scissors" and  computer_input == "paper" or user_input == "paper" and computer_input == "rock":
    print("You win")
