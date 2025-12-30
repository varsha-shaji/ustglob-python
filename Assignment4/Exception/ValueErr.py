#2.	Write a program that accepts user input and handles 
# a ValueError if the input is not an integer.
try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(f"You entered : {number}")
except ValueError:
    print("Error: Please enter a valid integer.")