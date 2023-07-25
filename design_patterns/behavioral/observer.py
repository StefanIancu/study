# establishes a relationship subject - multiple observers

# subject to be monitored, observers to be notified when there's a change in the subject

class Subject(object):
    #represents what's being observed

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # if the observer not in observers list, append it
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # remove the observer
        try:
            self._observers.remove(observer)
        except ValueError as err:
            print(err)

    def notify(self, modifier=None):
        # alert the observers when there's a change in the subject
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property   #getter, gets the core temperature
    def temp(self):
        return self._temp
    
    @temp.setter  #setter, sets the core temperature
    def temp(self, temp):
        self._temp = temp 
        self.notify()

class TempViewer:

    def update(self, subject):
        print(f"Temp viewer: {c1._name} has temperature {c1.temp}")

# subjects 
c1 = Core("Core 1")
c2 = Core("Core 2")

# observers
v1 = TempViewer()   
v2 = TempViewer()

# attach observers to core 
c1.attach(v1)
c1.attach(v2)

# change temp of the core 
c1.temp = 80
c1.temp = 90
