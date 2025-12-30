#5.	Write a program to handle multiple exceptions in a single try block.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
