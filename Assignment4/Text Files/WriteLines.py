#1.	Write a Python program to create a 
# text file and write multiple lines into it.
file=open("lines.txt","w")
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")
file.close()

f=open("lines.txt","r")
content=f.read()
print(content)