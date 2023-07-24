# Singleton design pattern 

class Borg:

    _shared_data  = {} 

    def __init__(self):
        self.__dict__ = self._shared_data

class Singleton(Borg):

    def __init__(self, **kwargs):
        
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_data)
    
x = Singleton(HTTP = "Hyper Text Transfer Protocol")

print(x)

y = Singleton(SNMP = "Simple Network Management Protocol")

print(y)

# it keeps the first object and adds the y variable to it 

