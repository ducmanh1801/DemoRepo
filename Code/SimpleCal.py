import math
from Abstract import Operation

#ham cong
class Addition(Operation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

#ham tru
class Subtraction(Operation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b

#ham nhan
class Multiplication(Operation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b
#ham chia
class Division(Operation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            return "Error! Division by zero."
        return self.a / self.b
