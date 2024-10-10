# History list to store calculations
history = []

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# Function to display history and allow replay
def show_history():
    if not history:
        print("No history available.")
        return
    
    print("\nCalculation History:")
    for i, entry in enumerate(history):
        print(f"{i + 1}. {entry}")
    
    replay_choice = input("\nWould you like to replay any calculation? Enter the number or 'no' to skip: ")
    if replay_choice.lower() != "no":
        try:
            index = int(replay_choice) - 1
            if 0 <= index < len(history):
                print(f"\nReplaying calculation {index + 1}: {history[index]}")
            else:
                print("Invalid number. Returning to calculator.")
        except ValueError:
            print("Invalid input. Returning to calculator.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.View History")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"

        print(operation)
        history.append(operation)

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    elif choice == '5':
        show_history()

    else:
        print("Invalid Input")
