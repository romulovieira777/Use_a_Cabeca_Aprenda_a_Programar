dog_name = input("What's your dog's name? ")
dog_age = input("What's your dog's age? ")
dog_age_int = int(dog_age)
human_age = round(dog_age_int * 7)

print(f'Your dog {dog_name} is {human_age} years old in human years')
