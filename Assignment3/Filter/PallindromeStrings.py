words = ["madam", "python", "level", "hello", "radar"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)
