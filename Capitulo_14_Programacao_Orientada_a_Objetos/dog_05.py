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

    def human_years(self):
        human_age = self.age * 7
        return human_age

    def __str__(self):
        return "I'm a dog named " + self.name


class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler

    def walk(self):
        print(self.name, 'is helping its handler', self.handler, 'walk')


def print_dog(dog):
    print(dog.name + "'s", 'age is', dog.age, 'and his weight is', dog.weight)


codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)
rody = ServiceDog('Rody', 8, 38, 'Joseph')

print(codie)
print(jackson)
print(rody)
