#3.	How do you check if an element is present in a set?
s={10,20,30,40,50}
element=int(input("Enter element to check: "))
if element in s:
    print(f"{element} is present in the set.")
else:
    print(f"{element} is not present in the set.")