# bridge pattern helps untangle a class hierarchy 
# separate the abstraction into two different class hierarchies

class DrawingAPIOne(object):
    """concrete class one"""
    def draw_circle(self, x, y, radius):
        print(f"API 1 drawing a circle at {x}, {y} with {radius}!")

class DrawingAPITwo(object):
    """concrete class two"""
    def draw_circle(self, x, y, radius):
        print(f"API 2 drawing a circle at {x}, {y} with {radius}!")

class Circle(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
    
    def scale(self, percent):
        self._radius *= percent


# build first circle using API one
circle1 = Circle(1, 2, 3, DrawingAPIOne())

# draw a circle 
circle1.draw()

# build second circle 
circle2 = Circle(2, 3, 4, DrawingAPITwo())

# draw a circle 

circle2.draw()