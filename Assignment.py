# Basic Calculator Program

def main():
    # Ask the user to input two numbers
    num1 = float(input("Enter the first number: 20"))
    num2 = float(input("Enter the second number: 10"))
    
    # Ask the user to input the operation
    operation = input("Enter the operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))

    # Perform the operation based on the user's input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation.")
        return
    
    # Print the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()