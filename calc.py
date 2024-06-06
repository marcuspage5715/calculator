#!/usr/bin/env python3

def calculate(expression):
    try:
        # Evaluate the expression
        result = eval(expression)
        return result
    except Exception as e:
        return "Invalid input. Please use the format: number1 operator number2"

def main():
    while True:
        # Prompt for user input
        user_input = input("Enter calculation (or type 'Q', 'exit', or 'quit' to quit): ")

        # Check for exit conditions
        if user_input.lower() in ['q', 'exit', 'quit']:
            print("Exiting...")
            break

        # Perform calculation
        result = calculate(user_input)
        print("Result:", result)

if __name__ == "__main__":
    main()

