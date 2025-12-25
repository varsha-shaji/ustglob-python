#1.	How would you create a new list of squares from an existing
# list of numbers using list comprehension?
numbers = [1, 2, 3, 4, 5]
print("Existing list : ",numbers)
squares = [x*x for x in numbers ]
print("Squares of each number from existing list :",squares)
