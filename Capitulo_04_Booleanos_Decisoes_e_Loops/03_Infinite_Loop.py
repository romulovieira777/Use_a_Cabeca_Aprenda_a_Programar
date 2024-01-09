# Infinite Loop
# The loop will never end because counter will always be greater than 0.

counter = 10

while counter > 0:
    print(f'Counter is {counter}')
    counter += 1

print('Liftoff!')

# Correct Loop
counter = 10

while counter > 0:
    print(f'Counter is {counter}')
    counter -= 1

print('Liftoff!')
