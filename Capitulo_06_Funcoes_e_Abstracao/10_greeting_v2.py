def greet(name, emoticon, message='You role!'):
    print('Hi', name + '.', message, emoticon)


greet('John', ':-)')
greet('Jennifer', ':-D', 'How are you today?')
greet(message='Where have you been?', name='Jill', emoticon='thumbs up')
greet('Betty', message='Yo!', emoticon=':)')
