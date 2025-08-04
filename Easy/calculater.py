# calculator.py
# A simple command-line calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def show_menu():
    print("""
============================
      PYTHON CALCULATOR
============================
Hello king, choose an operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
0. Exit
""")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0–4): ").strip()

        if choice == '0':
            print("You are now exiting, king. Stay sharp.")
            break

        if choice in {'1', '2', '3', '4'}:
            try:
                x = float(input("Enter the first number, king: "))
                y = float(input("Enter the second number, king: "))
            except ValueError:
                print("Error: Input must be a number.")
                continue

            result = {
                '1': add,
                '2': subtract,
                '3': multiply,
                '4': division
            }[choice](x, y)

            print("Result:", result)
        else:
            print("Invalid option, king. Try again.")

if __name__ == "__main__":
    main()
