def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


menu = """
Select operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
"""

while True:
    choice = input("Enter the number of the operation your choice (1, 2, 3, 4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("you have to enter an actual number please!")
            continue

        # if choice == '1':
        #     print(num1, "+", num2, "=", add(num1, num2))

        # elif choice == '2':
        #     print(num1, "-", num2, "=", subtract(num1, num2))

        # elif choice == '3':
        #     print(num1, "*", num2, "=", multiply(num1, num2))

        # elif choice == '4':
        #     print(num1, "/", num2, "=", divide(num1, num2))

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))
        
        next_calculation = input("do you want to take another calculation? (yes/no): ").lower()
        if next_calculation == "no":
          break
    else:
        print("you have to enter an actual number please!")