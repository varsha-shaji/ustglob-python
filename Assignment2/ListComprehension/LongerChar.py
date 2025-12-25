#3.	Write a list comprehension to extract 
# all words that are longer than 4 characters from a sentence.
sentence = "Python list comprehension is very powerful"
long_words = [word for word in sentence.split() if len(word) > 4]
print(long_words)