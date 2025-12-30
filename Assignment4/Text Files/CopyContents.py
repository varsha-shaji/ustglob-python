#4.	Write a program to copy the 
# contents of one text file into another file.
with open("lines.txt", "r") as source_file:
    with open("data.txt", "w") as dest_file:
        for line in source_file:
            dest_file.write(line)

with open("data.txt", "r") as file:
    print(file.read())