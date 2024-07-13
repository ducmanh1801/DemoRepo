import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return math.pow(a, b)

def sqrt(a):
    if a < 0:
        return "Error! Square root of negative number."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error! Factorial of negative number."
    return math.factorial(a)

def log(a):
    if a <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(a)

def main():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {power(num1, num2)}")

    elif choice == '6':
        num = float(input("Enter the number: "))
        print(f"The result is: {sqrt(num)}")
 
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
