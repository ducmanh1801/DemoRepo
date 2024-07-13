import math
from Abstract import Operation
from SimpleCal import *
from Calculation import *
def main():
    operations = []
    results = set()
    
    print("Welcome to the Math Functions Application")
    print("Select the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Logarithm")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        pair = (num1, num2)

        if choice == '1':
            operation = Addition(num1, num2)
        elif choice == '2':
            operation = Subtraction(num1, num2)
        elif choice == '3':
            operation = Multiplication(num1, num2)
        elif choice == '4':
            operation = Division(num1, num2)
        elif choice == '5':
            operation = Power(num1, num2)
        
        operations.append(pair)

    elif choice in ['6', '7', '8']:
        num = float(input("Enter the number: "))
        pair = (num,)

        if choice == '6':
            operation = SquareRoot(num)
        elif choice == '7':
            operation = Factorial(int(num))
        elif choice == '8':
            operation = Logarithm(num)
        
        operations.append(pair)
    else:
        print("Invalid Input")
        return

    result = operation.execute()
    results.add(result)
    print(f"The result is: {result}")
    print(f"Operations performed: {operations}")
    print(f"Unique results: {results}")


