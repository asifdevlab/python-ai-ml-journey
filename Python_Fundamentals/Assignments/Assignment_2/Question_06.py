# Question 6:
# Write a program to print all numbers from 1 to 100
# that are divisible by both 3 and 5.

print("All the numbers between 1 to 100 that are divisible by 3 and 5 both are as follows: ")
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)
