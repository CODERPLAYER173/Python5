import random


print("welcome to the number guessing game, I am thinking of a number between 1-100")
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
level = input("do you want to play hard or easy type it").lower()
number = random.choice(list_number)
if level == "hard":
    def check_hard(lives):
        guess = int(input("enter your guess"))
        if guess == number:
            print("you guessed right")
        elif guess > number:
            lives -= 1
            print(f'too high \nyou have {lives} guesses remaining')
        elif guess < number:
            lives -= 1
            print(f'too low \nyou have {lives} guesses remaining')
        while lives > 0:
            guess = int(input("enter your guess"))
            if guess == number:
                print("you guessed right")
            elif guess > number:
                lives -= 1
                print(f'too high \nyou have {lives} guesses remaining')
            elif guess < number:
                lives -= 1
                print(f'too low \nyou have {lives} guesses remaining')
    check_hard(lives=5)




elif level == "easy":
    def check_hard(lives):
        guess = int(input("enter your guess"))
        if guess == number:
            print("you guessed right")
        elif guess > number:
            lives -= 1
            print(f'too high \nyou have {lives} guesses remaining')
        elif guess < number:
            lives -= 1
            print(f'too low \nyou have {lives} guesses remaining')
        while lives > 0:
            guess = int(input("enter your guess"))
            if guess == number:
                print("you guessed right")
            elif guess > number:
                lives -= 1
                print(f'too high \nyou have {lives} guesses remaining')
            elif guess < number:
                lives -= 1
                print(f'too low \nyou have {lives} guesses remaining')
    check_hard(lives=10)
