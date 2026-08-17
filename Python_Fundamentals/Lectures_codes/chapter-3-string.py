# ============================================
# STRING IN PYTHON
# Chapter 3 - STRINGS
# Author: Asif Hussain
# ============================================

# String creation
str1 = "hello world"
str2 = "Prime"

# Different Functions
# len() function returns the length of the string

word = "Prime"
print(len(word)) # 5

# Concatenation (Adding two strings)
first_name = "Asif"
last_name = "Hussain"

full_name = first_name + " " + last_name #concatenation
print(full_name)

# Loops on Strings
s = "Python"
for ch in s: # ch will store individual chars - 'P', 'y', 't', & so on
    print(ch)

# Indexin in strings
s = "Python"
print(s[0]) # 'P'
print(s[3]) # 'h'
print(s[-1]) # 'n' (negative index: last character)

# Slicing in strings
# string[start : stop : step]

s = "Python"
print(s[0:3]) # "Pyt"
print(s[2:]) # "thon"
print(s[:3]) # "Pyt"
print(s[::2]) # "Pto" (every second char)
print(s[::-1]) # "nohtyP" (reversed string)

# String Formatting
# Using format()

name = "Asif"
age = 24

text = "My name is {} and I am {} years old".format(name, age)
print(text)

text = "My name is {name} and I am {age} years old".format(name = "Ajay", age = 22) # Using named placeholder

print(text)

# Using f-strings
name = "Asif"
age = 24

text = f"My name is {name} and I am {age} years old"
print(text)

a = 5
b = 10
print(f"sum of {a} & {b} = {a + b}")
print(f"avg of {a} & {b} = {(a  + b) / 2}")


