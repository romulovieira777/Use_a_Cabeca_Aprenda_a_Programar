characters = 'taco'

output = ''
length = len(characters)

i = 0

while i < length:
    output += characters[i]
    i += 1

length = length * -1
i = -2

while i >= length:
    output += characters[i]
    i -= 1

print(output)
