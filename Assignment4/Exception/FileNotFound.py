#3.	Write a program to open a file and handle a FileNotFoundError.
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: The file was not found.")
