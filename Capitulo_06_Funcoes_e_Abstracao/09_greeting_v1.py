greeting = 'Greetings'


def greet(name, mesage):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', mesage)


greet('June', 'See you soon!')
print(greeting)
