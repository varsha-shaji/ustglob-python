num1=eval(input("Enter first number: "))
num2=eval(input("enter second number : "))
try:
    result=num1/num2
    print("The result is:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")