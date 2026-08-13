# Question 5:
# Write a function to return the sum of digits of a number n.

def digit_sum(n):
    sum = 0
    while(n != 0):
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

num = int(input("Enter a number to get the sum of it's digits: "))

print(f"Sum of digits of {num} is {digit_sum(num)}")