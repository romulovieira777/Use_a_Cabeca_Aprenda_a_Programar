def get_bark(weight):
    if weight > 20:
        return 'says WOOF WOOF'
    else:
        return 'says woof woof'


codies_bark = get_bark(40)
print("Codie's bark is:", codies_bark)


def make_greeting(name):
    return 'Hi ' + name + '!'


print(make_greeting('Benjamin'))


def compute(x, y):
    total = x + y
    if total > 10:
        total = 10
    return total


print(compute(2, 3))
print(compute(11, 3))


def allow_access(person):
    if person == 'Dr Evil':
        answer = False
    else:
        answer = True
    return answer


print(allow_access('Codie'))
print(allow_access('Dr Evil'))
