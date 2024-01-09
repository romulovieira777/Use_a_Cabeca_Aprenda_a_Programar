color = 'blue'
guess = ''
guesses = 0

while guess != color:
    guess = input('What color am I thinking of? ')
    guesses += 1

if guesses == 1:
    print(f'You got it! It took you {guesses} guess.')
else:
    print(f'You got it! It took you {guesses} guesses.')
