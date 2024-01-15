def get_user_input(prompt, default):
    user_input = input(f"{prompt} [{default}]? ").strip()
    return user_input if user_input else default


hair = get_user_input("What color hair", "brown")
print("You chose", hair)

hair_length = get_user_input("What hair length", "short")
print("You chose", hair_length)

eyes = get_user_input("What eye color", "blue")
print("You chose", eyes)

gender = get_user_input("What gender", "female")
print("You chose", gender)

has_glasses = get_user_input("Has glasses", "no")
print("You chose", has_glasses)

has_beard = get_user_input("Has beard", "no")
print("You chose", has_beard)
