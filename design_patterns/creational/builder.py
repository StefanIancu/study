# Solution to an anti-pattern 

# building cars 

# the builder orders and removes all the unecessary parts in building an object 
# reducing the complexity of building an object 

class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car



class Builder():

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Diesel"

class Car():

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self) -> str:
        return "{} | {} | {}".format(self.model, self.tires, self.engine)
    
builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)

# creating another concrete builder 

class Mustang(Builder):

    def add_model(self):
        self.car.model = "Mustang"

    def add_tires(self):
        self.car.tires = "Michelin"

    def add_engine(self):
        self.car.engine = "V8"

builder2 = Mustang()
director2 = Director(builder2)
director2.construct_car()
car2 = director2.get_car()

print(car2)
