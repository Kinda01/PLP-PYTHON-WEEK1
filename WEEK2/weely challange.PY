def basic_calculator():
    print("Welcome to the Basic Calculator! 🧮")
    
    # Get user input for the numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Get user input for the operation
    print("\nChoose an operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == "+":
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == "/":
        # Handle division by zero
        if num2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation! Please enter one of +, -, *, or /.")
    
    print("\nThank you for using the Basic Calculator!")

# Run the calculator function
basic_calculator()
