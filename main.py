def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    while True:
        operation = input("Enter the operation you want to perform (+, -, *, or /): ")
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation.")

        print("The result is:", result)

        again = input("Do you want to calculate again? (Y/N): ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()