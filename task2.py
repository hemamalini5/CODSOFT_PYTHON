def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x, y):
    return x * y 
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by Zero "
def calculator():
    print("Welcome to  the Simple Calculator ")
    print("Select an Operation ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4.Division (/)")

    #Get user input 
    operation = input("Enter the operation (1/2/3/4):")

    #Validate operation choice 
    if operation in ['1','2','3','4']:
        try:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return
        
        if operation == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = add(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = add(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            result = add(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Operation choice! PLease enter a valid operation.")

if __name__ == "__main__":
    calculator()