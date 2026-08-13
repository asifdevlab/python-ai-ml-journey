# Question 4:
# Write a function to return the count of digits in a number n.

def digit_counter(n):
    count = 0
    while(n != 0):
        n = n // 10
        count += 1
    return count

num = int(input("Enter a number to know number of digits it contains: "))

print(f"Number of digits {num} contains are {digit_counter(num)}")