# Question 6:
# Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example: {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]
print("The list of fruits:")
print(words)
print()

words_dictionary = {}
for fruit in words:
    words_dictionary[fruit] = len(fruit)

print("Converted list of fruits into dictionary with their lenght:")
print(words_dictionary)