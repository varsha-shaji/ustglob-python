#3.	How would you use the map() function to convert all string elements of a list to uppercase?
words = ["python", "java", "c++"]
upper_words = list(map(str.upper, words))
print(upper_words)
