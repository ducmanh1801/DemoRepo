import math
from Abstract import Operation

class Power(Operation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return math.pow(self.a, self.b)

class SquareRoot(Operation):
    def __init__(self, a):
        self.a = a

    def execute(self):
        if self.a < 0:
            return "Error! Square root of negative number."
        return math.sqrt(self.a)

class Factorial(Operation):
    def __init__(self, a):
        self.a = a

    def execute(self):
        if self.a < 0:
            return "Error! Factorial of negative number."
        return math.factorial(self.a)

class Logarithm(Operation):
    def __init__(self, a):
        self.a = a

    def execute(self):
        if self.a <= 0:
            return "Error! Logarithm of non-positive number."
        return math.log(self.a)
