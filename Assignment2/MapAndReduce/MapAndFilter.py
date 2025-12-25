numbers = [1, 2, 3, 4, 5, 6]

mapped = list(map(lambda x: x * 2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))

print("Map result:", mapped)
print("Filter result:", filtered)

