num1 = int(input("enter the first number\n"))
operator = str(input("operator + - * / \n"))
num2 = int(input("enter the second number\n"))

match operator:
    case "+":
        print("Addition of two number", num1+num2)
    case "-":
        print("Substract of two number", num1-num2)
    case "*":
        print("multiply of two number", num1*num2)
    case "/":
        print("Divide of two number", num1+num2)
    case _:
        print("No Action end of program ")