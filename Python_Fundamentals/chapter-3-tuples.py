# ============================================
# PYTHON FUNDAMENTALS
# Chapter 3 - TUPLES
# Author: Asif Hussain
# ============================================

# Tuple creation
tup = (10, 20, 30)

print(tup)
print(type(tup)) # < class 'tuple'>

empty_tuple = () # empty tuple
single_elment_tuple = (43,)

# Indexing & Slicing
t = (10, 20, 30, 40)

print(t[0]) # 10
print(t[-1]) # 40
print(t[1:3]) # (20, 30)

# Loops on tuples
t = (10, 20, 30, 40)

for val in t:
    print(val)

# Using loops to calculate sum of all elements of the tuple:
t = (10, 8, 9)

sum = 0
for val in t:
    sum += val

print("Sum:", sum)

# Tuple Methods
# index(val) returns index of first occurence for any value
# count(val) - returns total count of occurence for any value

t = (1, 3, 4, 3, 2)

print(t.index(3)) # 1
print(t.count(3)) # 2






