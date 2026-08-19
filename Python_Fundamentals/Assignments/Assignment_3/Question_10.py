# Question 10:
# Ask the user for a string and print:
# • All unique characters
# • The count of unique characters

text = input("Enter a string: ").lower()

unique = ""

for character in text:
    if character not in unique:
        unique += character

print("Unique character:")
for ch in unique:
    print(ch)

print("Count of unique character:", len(unique))