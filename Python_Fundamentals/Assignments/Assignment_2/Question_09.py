# Question 9:
# Write a function is_prime(n) that returns True if n is prime,
# and False otherwise, using a loop.
# Hint:
# - Prime check only for n >= 2 (2 is the smallest prime).
# - A non-prime number will always be divisible by at least one number in [2, n-1].

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to know whether it is prime or not: "))

print(f"The given number is Prime: {is_prime(num)}")
