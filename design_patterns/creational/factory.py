# Factory pattern 

# when not sure about the type of objects needed in the sys

# decisions needs to be made at runtime

class Dog():

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"
    
def get_pet(pet="dog"):

    """Factory method"""
    pets = dict(dog=Dog("Hope"))
    return pets[pet]

class Cat():

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"
    
def get_pet(pet="dog"):

    """Factory method"""
    pets = dict(dog=Dog("Hope"),cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())