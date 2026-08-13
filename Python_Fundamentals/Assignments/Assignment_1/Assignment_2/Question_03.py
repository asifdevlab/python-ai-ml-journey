# Question 3:
# Write a function that prints the digits of a number n.
# Example: For n = 312, output should be 3, 1, 2.
# Hint: The rightmost digit of N is N % 10.
# To remove the rightmost digit, do N = N / 10.

def digit_printer(n):
    while(n != 0):
        digit = n % 10
        print(digit)
        n = n // 10
        
num = int(input("Enter a number to get it's digits printed: "))
digit_printer(num)
