# Harshitha's CS50 Calculator Project

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Main function starts here
def main():
    print("Hi! I'm Harshitha, and this is my CS50 Final Project: a Python Calculator.")
    print("You can use it to add, subtract, multiply, or divide numbers.")
    print("Type 'about' to learn about me, or 'exit' to quit.\n")

    while True:
        # Ask user which operation they want to perform
        operation = input("What would you like to do? (add/subtract/multiply/divide/about/exit): ").strip().lower()

        if operation == "exit":
            print("Thanks for using Harshitha's Calculator. Goodbye!")
            break

        elif operation == "about":
            print("\n This calculator was built by Harshitha Tiwari as her CS50x final project.")
            print("I created this to learn Python and build something useful!\n")
            continue

        elif operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Please try again.\n")
            continue

        # Ask for numbers
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("That wasn't a valid number. Please enter digits only.\n")
            continue

        # Perform the selected operation
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)

        # Show the result
        print(f"Result: {result}\n")

# Call the main function to start the program
if __name__ == "__main__":
    main()

