# converts the interface of a class into another one the client expects

from typing import Any


class Korean:
    """korean speaker"""
    
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"
    
class British:
    """english speaker"""

    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"
    
class Adapter:

    def __init__(self, object, **adapted_method):
        """change the name of the method """
        self._object = object 

        # new dict item that establishes the mapping between methods
        # speak() will be translated to speak_korean() if speaker == Korean
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """return the rest of attributes"""
        return getattr(self._object, attr)
    
# list to store speaker objects 
objects = []

# create a Korean object 
korean = Korean()

# create a British object
british = British()

# append the objects to the objects list 
objects.append(Adapter(korean, speak=korean.speak_korean()))
objects.append(Adapter(british, speak=british.speak_english()))

for obj in objects:
    print(f"{obj.name} says {obj.speak}")