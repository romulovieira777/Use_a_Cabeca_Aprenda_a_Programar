class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says WOOF! WOOF!')
        else:
            print(self.name, 'says woof! woof!')
