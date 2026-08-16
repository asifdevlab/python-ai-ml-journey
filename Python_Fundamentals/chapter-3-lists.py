# ============================================
# PYTHON FUNDAMENTALS
# Chapter 3 - LISTS
# Author: Asif Hussain
# ============================================

# Creation of list
'''my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list)) # <class 'list'>

my_list2 = [10, "Hello", 3.14, True, 10] # hetrogenous list
print(my_list2)

# List Indexing

# Access Elements
my_list = ["apple", "banana", "cherry"]
print(my_list[0]) # apple
print(my_list[1]) # banana
print(my_list[-1]) #  cherry (last element)

# Modify Elements
my_list = [1, 2, 3, 4]
my_list[0] = 10
print(my_list) # [10, 2, 3, 4]

# Slicing 
# list[start:end:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Simple Slice
print(numbers[2:5]) # Output: [2, 3, 4]

print(numbers[:4]) # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[5:]) # Output: [5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[:]) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,] (copy of the whole list)

#Using step
print(numbers[::2]) #Ouput: [0, 2, 4, 6, 8] (every second element)
print(numbers[1::3]) #Output: [1, 4, 7] (Start at 1, every 3rd element)

# Negative Slicing
print(numbers[-5:-2]) # Output: [5, 6, 7] (negative indexing from end)

# List Methods
nums = [5, 2, 9]
print(len(nums)) # 3

nums.append(7)
print(nums) # [5, 2, 9, 7]

nums.insert(1, 4)
print(nums) # [5, 4, 2, 9, 7]

nums.sort()
print(nums) # [2, 4, 5, 7, 9]

nums.reverse()
print(nums) # [9, 7, 5, 4, 2]

nums.sort(reverse= True) # for sorting list into descending order
print(nums)

# Loops on Lists
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)'''

# Linear Search
numbers = [5,12, 7, 3, 18, 9]
x = 18
idx = 0

for num in numbers:
    if num == x:
        print(f"{x} is found at index {idx}")
        break
    idx += 1

