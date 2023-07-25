# new features to an existing class hierarchy without changing it 

class House(object):
    #class being visited
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__
    
class Visitor(object):

    def __str__(self):
        return self.__class__.__name__
    
class HvacSpecialist(Visitor):

    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):

    def visit(self, house):
        house.work_on_electricity(self)

# hvac-specialist
hv = HvacSpecialist()

# electrician 
e = Electrician()

# house 
home = House()

# let the house accept the HVAC and let him work on the house 
home.accept(hv)

# let the house accept the electrician
home.accept(e)