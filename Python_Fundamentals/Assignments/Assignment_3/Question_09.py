# Question 9:
# Given a list, print all elements that appear more than once in the list.
# Hint: Use sets.

numbers = [1, 2 , 3, 2, 4, 1, 5, 2]

seen = set()
duplicates = set()

for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print("Duplicate elements:", duplicates)
