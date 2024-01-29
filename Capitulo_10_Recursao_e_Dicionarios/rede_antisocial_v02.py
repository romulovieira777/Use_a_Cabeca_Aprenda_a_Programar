attributes = {
    'email': 'kim@oreilly',
    'gender': 'f',
    'age': 27,
    'friends': ['John', 'Josh']
}

users = {}

users['Kim'] = attributes
users['John'] = {
    'email': 'john@abc.com',
    'gender': 'm',
    'age': 24,
    'friends': ['Kim', 'Josh']
}
users['Josh'] = {
    'email': 'josh@wickedlysmart.com',
    'gender': 'm',
    'age': 32,
    'friends': ['Kim']
}


def average_age(user_name):
    """Calcula a idade média dos amigos de um usuário."""
    user = users[user_name]
    ages = []
    for friend in user['friends']:
        ages.append(users[friend]['age'])
        average_age_value = sum(ages) / len(ages)
    print(f"{user_name}'s friends have an average age of {average_age_value:.1f}")


average_age('Kim')
average_age('John')
average_age('Josh')


max = 1000

for name in users:
    user = users[name]
    friends = user['friends']
    if len(friends) < max:
        most_anti_social = name
        max = len(friends)

print('The most anti-social user is:', most_anti_social)
