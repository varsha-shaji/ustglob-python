#1.	How does the map() function work in Python?
# Give an example where you square each number in a list.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)
