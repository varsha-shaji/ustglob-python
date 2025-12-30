#5.	Write a Python program to search for a 
# specific word in a text file and display 
# the line numbers where it appears.
word= "Python"  # Replace with the word you want to search
with open("lines.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.__contains__(word):
            print(f"Found '{word}' in line {lines.index(line) + 1}: {line.strip()}")
            break
        else:
            print(f"'{word}' not found.")
            break
