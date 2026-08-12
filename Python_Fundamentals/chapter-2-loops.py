# ============================================
# LOOPS IN PYTHON
# Chapter 2 - While Loops
# Author: Asif Hussain
# ============================================


# --------------------------------------------
# INFINITE LOOP
# --------------------------------------------

# WARNING:
# Infinite loops continue forever until stopped manually.

while True:
    print("Hello World")


# --------------------------------------------
# FINITE LOOP
# --------------------------------------------

print("Finite Loop Example")

i = 1   # Iterator

while i <= 5:
    print("Hello World", i)
    i += 1

print("After loop, i =", i)


# --------------------------------------------
# PRINT NUMBERS FROM 1 TO 5
# --------------------------------------------

print("\nNumbers from 1 to 5")

i = 1

while i <= 5:
    print(i)
    i += 1


# --------------------------------------------
# COUNTING IN REVERSE
# --------------------------------------------

print("\nReverse Counting from 10 to 1")

i = 10

while i >= 1:
    print(i)
    i -= 1


# --------------------------------------------
# MULTIPLICATION TABLE
# --------------------------------------------

num = int(input("\nEnter a number: "))

print("\nMultiplication Table of", num)

i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

#-------------------
#Break and Continue
#-------------------

i = 1

while (i <= 10):
    if (i % 6 == 0):
        break
    print(i)
    i += 1

print("Outside loop now....")

#Use of continue

i = 1

while (i <= 10):
    if (i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1

print("Outside loop...")

# Print all the odd numbers from 1-10
i = 1

while (i <= 10):
    print(i)
    i += 2

#Using continue
i = 0

while (i < 10):
    i += 1
    if (i % 2 == 0):
        continue
    print(i)

#For Loop
for i in range(5):
    print(i)
#output: 0,1,2,3,4"""


#Membership Operator

'''word = "Prime"

# Example 1 - Looping over a string
for ch in word:
    print(ch)

# Example 2 - Check if char 'i' exists in word
if 'i' in word:
    print("letter exists")

# Example 3 - Count number of 'i' in the word
word = "artificial intelligence"
count = 0

for ch in word:
    if ch == 'i':
        count += 1

print(f"i occurs {count} times.")

# Nested Loops
for i in range(1, 3):
    for j in range(1, 3):
        print(f"({i}, {j})")

# Range Function

# Single Argument - start
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4

# 2 arguments - start, stop
for i in range(1,6):
    print(i)

# output: 1, 2, 3, 4, 5

# 3 arguments - start, stop, step
for i in range(1,10,2):
    print(i)

#output: 1, 3, 5, 7, 9

# Practice Problem (set 2)
#1. Print multiplication table for any number n. [using while]

n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# Print odd numbers from 1 to 10, using continue. [using while].

i = 1

while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
# 3. Count vowels in a word. [using for]

word = str(input("Enter a word: "))
count = 0
for ch in word:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == "u"):
        count += 1

print(f"Number of vowels in given word is {count}")

# 4. Sum of first n natural numbers. [using for]

n = int(input("Enter a number: "))
sum = 0

for i in range(1,n+1):
    sum += i

print("Sum =", sum)



    






    


