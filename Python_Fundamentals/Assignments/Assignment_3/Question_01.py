# Question 1:
# Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is the same when read forward & backward.
# Example: "madam", "racecar".
# Hint: A palindrome string is equal to the reversed version of the string.

word = input("Enter a word: ")

# Convert to lowercase for comparison
word = word.lower()

# Check if the word is equal to its reverse
if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")