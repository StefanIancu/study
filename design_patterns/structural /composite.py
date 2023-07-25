# maintains a tree data structure to represent relationships 

# component (abstract) - child (concrete inherits from component) - composite (concrete inherits from component)

class Component(object):
    """abstract class"""

    def __init__(self, *args, **kwargs):
        pass


    def component_function(self):
        pass

class Child(Component):
    """concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

    def component_function(self):
        print(f"{self.name}")

class Composite(Component):
    """concrete class - maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # store the name of the composite object
        self.name = args[0]

        # keeping the child items 
        self.children = []

    def append_child(self, child):
        """method to add new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """method to remove a child"""
        self.children.remove(child)

    def component_function(self):
        print(f"{self.name}")

        for i in self.children:
            i.component_function()
        
# build a composite submenu 1
sub1 = Composite("submenu1")

# new child sub_submenu11 and 12
sub11 = Child("sub_submenu11")
sub12 = Child("sub_submenu12")

# add children to submenu 1
sub1.append_child(sub11)
sub1.append_child(sub12)

# build a top level composite menu
top = Composite("top_menu")

# build a submenu2
sub2 = Child("submenu2")

# add composite submenu 1 to top level menu
top.append_child(sub1)

# add submenu 2 to top level menu
top.append_child(sub2)

# test composite pattern 
top.component_function()