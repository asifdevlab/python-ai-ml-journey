# Question 2:
# Given a list of integers, compute the average of all numbers in the list.

numbers = [4, 5, 6, 8]

total = 0
for num in numbers:
    total += num

avg_list = total / len(numbers)
print(f"Average of the numbers in list is {avg_list}")


    