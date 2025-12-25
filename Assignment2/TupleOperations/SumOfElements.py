#5.	Write a Python function that takes a tuple of numbers and returns the sum of all its elements.
def sum_of_elements(tup):
    return sum(tup)

# Example usage
nums=tuple(map(int,input("Enter numbers separated by spaces: ").split()))
result = sum_of_elements(nums)
print("Sum of elements:", result)