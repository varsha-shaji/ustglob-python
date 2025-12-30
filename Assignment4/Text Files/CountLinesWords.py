#3.	Write a Python program to count the
# number of lines, words, and characters in a text file.
try:
    with open("data.txt", 'r') as file:
        text = file.read()

    lines = text.split('\n')
    words = text.split()
    characters = len(text)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

except FileNotFoundError:
    print("File not found.")
