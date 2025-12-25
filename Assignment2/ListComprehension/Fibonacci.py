#4.	How can you use list comprehension to generate a list of the first 10 Fibonacci numbers?
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)
