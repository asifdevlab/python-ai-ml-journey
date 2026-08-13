# Question 2:
# Write a function that takes two integers a and b
# and prints all even numbers between them (inclusive).

def even_number_print(a,b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
            i += 1

print("Enter two numbers to get all the even numbers between them.")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print(f"All the even numbers between {num1} and {num2} are as follows:")

even_number_print(num1,num2)


