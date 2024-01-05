import random


user_choice = input('Choose rock, paper or scissors: ')
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

print(f'You choose {user_choice}, and the computer choose {computer_choice}.')
