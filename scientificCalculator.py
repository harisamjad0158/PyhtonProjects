import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def trig_functions(x, operation):
    radians_value = math.radians(x)
    if operation == "sin":
        return math.sin(radians_value)
    elif operation == "cos":
        return math.cos(radians_value)
    elif operation == "tan":
        return math.tan(radians_value)
    elif operation == "asin":
        return math.asin(radians_value)
    elif operation == "acos":
        return math.acos(radians_value)
    elif operation == "atan":
        return math.atan(radians_value)

def main():
    print("Welcome to the Scientific Calculator!")

    while True:
        print("\nSelect Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Trigonometric Functions")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Result:", add(x, y))
        elif choice == "2":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Result:", subtract(x, y))
        elif choice == "3":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Result:", multiply(x, y))
        elif choice == "4":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Result:", divide(x, y))
        elif choice == "5":
            x = float(input("Enter the base: "))
            y = float(input("Enter the exponent: "))
            print("Result:", power(x, y))
        elif choice == "6":
            x = float(input("Enter the number: "))
            print("Result:", square_root(x))
        elif choice == "7":
            x = float(input("Enter the number: "))
            base = float(input("Enter the base (default is 10): "))
            print("Result:", logarithm(x, base))
        elif choice == "8":
            x = float(input("Enter the angle in degrees: "))
            operation = input("Select operation (sin/cos/tan/asin/acos/atan): ")
            print("Result:", trig_functions(x, operation))
        elif choice == "9":
            print("Thank you for using the Scientific Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
