
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

user_cards = random.choices(cards,k=2)
print(f'Your cards{user_cards}')
computer_cards = random.choices(cards,k=2)
computer_cards_user = random.choice(computer_cards)
print(f'computer\'s one card {computer_cards_user}')
user_card_ = sum(user_cards)
computer_card_ = sum(computer_cards)

if user_cards == [11, 10] or user_cards == [10, 11]:
    print("you win yay🎉🎉🎉🎉🎉")
elif user_cards == [11, 10] or user_cards == [10, 11]:
    print("The computer wins you lose")

if user_card_ > 21:
    for ace in user_cards:
        if ace == 11:
            user_card_ = user_card_ -10
            if user_card_ > 21:
                print("You lose")
elif user_card_ < 21:
    draw = input("Do you want to draw more cards type Y or N for yes and no respectively").upper()
    while draw == "Y":
        n_card = random.choice(cards)
        user_cards .append(n_card)
        print(f'Your cards {user_cards}')
        user_card_ = sum(user_cards)
        computer_card_ = sum(computer_cards)
        if user_card_ == 21:
            print("you win yay🎉🎉🎉🎉🎉")
        elif user_card_ == 21:
            print("The computer wins you lose ")

        if user_card_ > 21:
            for ace in user_cards:
                if ace == 11:
                    user_card_ = user_card_ - 10
                    if user_card_ > 21:
                        print("You lose as ")
                elif ace != 11:
                    print("")
        draw = input("Do you want to draw more cards type Y or N for yes and no respectively").upper()
        break
    while draw == "N":
        if user_card_ == 21:
            print("you win yay🎉🎉🎉🎉🎉")
        elif user_card_ == 21:
            print("The computer wins you lose ")
        if computer_card_ < 17:
            n_card = random.choice(cards)
            computer_cards .append(n_card)
            computer_card_ = sum(computer_cards)
            if computer_card_ > 21:
                print("you win  ")
        elif computer_card_ > 17:
            if user_card_ > computer_card_:
                print("You win ")
            elif user_card_ < computer_card_:
                print("You lose")
            else:
                print("Its a Draw")
            break
