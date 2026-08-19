# Question 7:
# Write a program that takes a string from the user
# and prints the number of spaces in the string.

sentence = input("Write a sentence: ")

count = 0
for ch in sentence:
    if ch == " ":
        count += 1

print(f"Number of spaces the sentence has {count}")
