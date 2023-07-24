# Prototype pattern - > clones objects 

# making a copy, instead of building 
# useful when instancing more obj which could be expensive in terms of computing power 

# create a prototypical instance first, then clone it when you need a replica 

import copy

class Prototype():

    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
    
class Car:

    def __init__(self):
        self.name = "Tesla"
        self.color = "Black"
        self.options = "Autopilot"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)
    
c = Car()
prototype = Prototype()
prototype.register_object("tesla", c)
c1 = prototype.clone("tesla")

print(c1)