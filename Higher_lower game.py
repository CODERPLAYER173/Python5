
import higher_lowergame_data
import random
r = random.randint(0,24)
n = random.randint(25,49)
score = 0
print(art.logo)
def data_a():
    account_name = game_data.data[r]['name']
    account_description = game_data.data[r]['description']
    account_country = game_data.data[r]['country']
    return print(f'Compare A {account_name}, a {account_description} from {account_country}')
def data_b():
    account_name = game_data.data[n]['name']
    account_description = game_data.data[n]['description']
    account_country = game_data.data[n]['country']
    return print(f'Compare B {account_name}, a {account_description} from {account_country}')

data_a()
print(art.vs)
data_b()
guess = input("Enter your guess who has more followers").lower()

while game_data.data[r]['follower_count'] > game_data.data[n]['follower_count'] and guess == "a":
    n = random.randint(25, 49)
    score += 1
    print(art.logo)


    def data_b():
        account_name = game_data.data[n]['name']
        account_description = game_data.data[n]['description']
        account_country = game_data.data[n]['country']
        return print(f'Compare B {account_name}, a {account_description} from {account_country}')
    data_a()
    print(art.vs)
    data_b()
    guess = input("Enter your guess who has more followers").lower()
while game_data.data[r]['follower_count'] < game_data.data[n]['follower_count'] and guess == "b":
    r = random.randint(0, 24)
    score += 1
    print(art.logo)

    def data_a():
        account_name = game_data.data[r]['name']
        account_description = game_data.data[r]['description']
        account_country = game_data.data[r]['country']
        return print(f'Compare A {account_name}, a {account_description} from {account_country}')

    data_a()
    print(art.vs)
    data_b()
    guess = input("Enter your guess who has more followers").lower()

if game_data.data[n]['follower_count'] > game_data.data[r]['follower_count'] and guess == "a":
    print("wrong guess your score is ",score)
elif game_data.data[n]['follower_count'] < game_data.data[r]['follower_count'] and guess == "b":
    print("wrong guess your score is ",score)
else:
    print("Pls enter a valid guess ")
