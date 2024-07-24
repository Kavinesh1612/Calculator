def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    return x / y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
            choice = int(input("Enter choice (1/2/3/4): "))
            if choice in (1, 2, 3, 4):
                break
            else:
                print("Please enter a valid number.")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        total = num1 + num2
        print("Addition :\n",num1,"+",num2,"=",total)
    elif choice == 2:
        total = num1 - num2
        print("Subtraction :\n",num1,"-",num2,"=",total)
    elif choice == 3:
        total = num1 * num2
        print("Multiplication :\n",num1,"*",num2,"=",total)
    elif choice == 4:
        total = num1 / num2
        print("Division :\n",num1,"/",num2,"=",total)

calculator()
