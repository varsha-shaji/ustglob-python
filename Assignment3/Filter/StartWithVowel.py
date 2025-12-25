words = ["apple", "banana", "orange", "grape", "umbrella"]

vowel_words = list(filter(lambda w: w[0].lower() in 'aeiou', words))

print(vowel_words)
