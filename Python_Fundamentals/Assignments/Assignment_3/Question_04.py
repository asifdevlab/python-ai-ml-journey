# Question 4:
# Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers

numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

even_tuple = tuple(even_list)
odd_tuple = tuple(odd_list)

print("Even numbers tuple:", even_tuple)
print("Odd numbers tuple:", odd_tuple)
