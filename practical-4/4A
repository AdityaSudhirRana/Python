class Calculator:
    def __init__(self, numa, numb, operation=None):
        self.a = numa
        self.b = numb
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            self.add()
        elif self.operation == "multiply":
            self.multiply()

    def add(self):
        print("Addition: ", self.a + self.b)
        
    def multiply(self):
        print("Multiplication: ", self.a * self.b)

class Calcexten(Calculator):
    def __init__(self, numa, numb):
        Calculator.__init__(self, numa, numb, operation=None)

    def calculate(self):
        if self.operation == "add":
            self.add()
        elif self.operation == "multiply":
            self.multiply()
        elif self.operation == "subtract":
            self.subtract()
        elif self.operation == "division":
                self.division()

    def subtract(self):
        print("Subtraction: ", self.a - self.b)
                    
    def division(self):
        print("Division: ", self.a / self.b)
        

calc1 = Calcexten(6, 3)
calc1.operation = "division"

calc1.calculate()
