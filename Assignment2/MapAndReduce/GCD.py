#4.	Write a Python program that uses reduce() 
# to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce
from math import gcd

numbers = [24, 36, 60]
result = reduce(gcd, numbers)
print("GCD:", result)
