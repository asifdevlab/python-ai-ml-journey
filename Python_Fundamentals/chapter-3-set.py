# ============================================
# PYTHON FUNDAMENTALS
# Chapter 3 - SET
# Author: Asif Hussain
# ============================================

# Set creation 
my_set = {1, 2, 2, 2, 3}

print(my_set) # {1, 2, 3}
print(type(my_set))
print(len(my_set)) # 3

empty_set = set() # for creating an empty set


# Set Methods
# 1. add(val) - adds an element to set 
# 2. remove(val) - removes an element(raises error if not found)
# 3. clear() - removes all elements
# 4. pop() - removes and return a random element (since sets are unordered)
# 5. s1.union(s2) - returns new union (union is collection of all unique values in both sets)
# 6. s1.intersection(s2) - returns new union (intersection is collection of all common & unique values in both sets)

s = {10, 20, 30}

s.add(40)
print(s) # {10, 20, 30, 40}

s.remove(10)
print(s) # {20, 30, 40}

print(s.pop()) # can be any value

s.clear()
print(s) # set() - empty set

#Union & Intersection
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B)) # {1, 2, 3, 4, 5}
print(A.intersection(B)) # {3}