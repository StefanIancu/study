import types

class Strategy:

    def __init__(self, function=None):
        self.name = "Default Strategy"

        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print(f"{self.name} is used!")

# replacement method 1
def strategy_one(self):
    print(f"{self.name} is used to execute method 1.")

# replacement method 2
def strategy_two(self):
    print(f"{self.name} is used to execute method 2.")

# default strategy
s0 = Strategy()

# execute strategy 
s0.execute()

# first variation of default strategy 
s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

# second variation of default strategy
s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()