# builds on the factory pattern 

# when the user expects a family of related obj, but doesn't have to know which family it is until runtime

class Dog():

    def speak(self):
        return "Woof"
    
    def __str__(self):
        return "Dog"
    
class DogFactory():

    def get_pet(self):
        return Dog()    
    
    def get_food(self):
        return "Dog Food"

class PetStore:

    def __init__(self, pet_factory = None):

        self._pet_factory = pet_factory

    def show_pet(self):

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}")

# create a concrete factory 
factory = DogFactory()

#create a pet store house our abstract factory 
shop = PetStore(factory)

shop.show_pet()