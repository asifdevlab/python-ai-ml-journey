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

    


