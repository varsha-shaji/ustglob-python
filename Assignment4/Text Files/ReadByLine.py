#2.	Write a program to read the contents of a text file line by line.
f=open("data.txt","r")
line=f.readline()
while line:
    print(line.strip())
    line=f.readline()
f.close()