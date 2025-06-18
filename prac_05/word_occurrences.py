"""
Damien Turner
CP1404 - Practical Solution
Program description: Counts repeated words in collection of words
Estimate: 20 minutes
Actual:   18 minutes
"""

text = input("Text: ")
words = text.split()
word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
