def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by 0"
    return a / b


operations = {
    1: ("Addition", add),
    2: ("Subtraction", subtract),
    3: ("Multiplication", multiply),
    4: ("Division", divide)
}


while True:
    print("\n--- Simple Calculator ---")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number (1-5)!")
        continue

    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in operations:
        print("Invalid choice! Please select from 1–5.")
        continue

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    operation_name, operation_func = operations[choice]
    result = operation_func(a, b)
    print(f"{operation_name} result: {result}")
