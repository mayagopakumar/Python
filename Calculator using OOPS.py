1class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    
calculator=Calculator()
    
while True:

    choice = input("""Enter choice
                   1. Addition
                   2. Subtraction
                   3. Multiplication
                   4. Division
                   """)
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            

        if choice == '1':
            print(num1, "+", num2, "=", calculator.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", calculator.sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", calculator.mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", calculator.div(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
