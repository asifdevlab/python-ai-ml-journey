# ============================================
# PYTHON FUNDAMENTALS - CHAPTER 1
# Author: Asif Hussain
# ============================================


# --------------------------------------------
# VARIABLES AND DATA TYPES
# --------------------------------------------

name = "Asif"
age = 25
pi = 3.14

print("Name:", name)
print("Age:", age)
print("Value of PI:", pi)
print("Data Type of PI:", type(pi))


# --------------------------------------------
# ARITHMETIC OPERATORS
# --------------------------------------------

a = 10
b = 5

print("\nArithmetic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)
print("Exponent:", a ** b)


# --------------------------------------------
# RELATIONAL OPERATORS
# --------------------------------------------

print("\nRelational Operators")
print(a < b)
print(a != b)
print(a == b)


# --------------------------------------------
# ASSIGNMENT OPERATORS
# --------------------------------------------

x = 10
x -= 5

print("\nAssignment Operator Result")
print(x)


# --------------------------------------------
# LOGICAL OPERATORS
# --------------------------------------------

print("\nLogical Operators")
print(not (5 > 8))
print((5 > 3) and (5 > 2))
print((5 > 3) and (5 > 8))
print((10 > 8) or (8 > 9))


# --------------------------------------------
# TYPE CONVERSION
# --------------------------------------------

num1 = 5
num2 = 10.0

result = num1 + num2

print("\nType Conversion")
print("Result:", result)
print("Data Type:", type(result))

explicit_conversion = int(result)

print("Converted to Integer:", explicit_conversion)
print("Data Type:", type(explicit_conversion))


# --------------------------------------------
# BOOLEAN TYPE CONVERSION
# --------------------------------------------

print("\nBoolean Conversion")
print(bool(0))
print(bool(10))


# --------------------------------------------
# USER INPUT
# --------------------------------------------

username = input("\nEnter your name: ")
print("Welcome", username)


# --------------------------------------------
# SUM OF TWO NUMBERS
# --------------------------------------------

first_number = int(input("\nEnter first number: "))
second_number = int(input("Enter second number: "))

sum_result = first_number + second_number

print("Sum =", sum_result)


# --------------------------------------------
# AVERAGE OF TWO NUMBERS
# --------------------------------------------

n1 = int(input("\nEnter first number: "))
n2 = int(input("Enter second number: "))

average = (n1 + n2) / 2

print("Average =", average)


# ============================================
# PRACTICE QUESTIONS
# ============================================


# --------------------------------------------
# QUESTION 1
# --------------------------------------------

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

print("Hello", name + ",", "you are", age, "years old!")


# --------------------------------------------
# QUESTION 2
# --------------------------------------------

num1 = int(input("\nEnter number 1: "))
num2 = int(input("Enter number 2: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Quotient =", num1 / num2)


# --------------------------------------------
# QUESTION 3
# --------------------------------------------

a = int(input("\nEnter integer 1: "))
b = int(input("Enter integer 2: "))
c = float(input("Enter a float value: "))

average = (float(a) + float(b) + c) / 3

print("Average =", average)


# --------------------------------------------
# QUESTION 4
# --------------------------------------------

num_str = "45"

num_int = int(num_str)
num_float = float(num_str)
num_string = str(num_str)

print("\nInteger Value:", num_int, "| Type:", type(num_int))
print("Float Value:", num_float, "| Type:", type(num_float))
print("String Value:", num_string, "| Type:", type(num_string))


# --------------------------------------------
# QUESTION 5
# --------------------------------------------

x = 10 + 3 * 2**2

print("\nValue of x =", x)


# --------------------------------------------
# QUESTION 6 - SWAPPING
# --------------------------------------------

num_1 = input("\nEnter first number: ")
num_2 = input("Enter second number: ")

print("\nBefore Swapping")
print("Number 1:", num_1)
print("Number 2:", num_2)

temp = num_1
num_1 = num_2
num_2 = temp

print("\nAfter Swapping")
print("Number 1:", num_1)
print("Number 2:", num_2)


# --------------------------------------------
# QUESTION 7 - TEMPERATURE CONVERSION
# --------------------------------------------

celsius = float(input("\nEnter temperature in Celsius: "))

fahrenheit = (celsius * (9 / 5)) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# --------------------------------------------
# QUESTION 8 - AREA OF CIRCLE
# --------------------------------------------

radius = float(input("\nEnter radius: "))

area = 3.14 * (radius ** 2)

print("Area of Circle =", area)


# --------------------------------------------
# QUESTION 9 - SIMPLE INTEREST
# --------------------------------------------

principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# --------------------------------------------
# QUESTION 10 - INTEGER & FRACTIONAL PART
# --------------------------------------------

num = float(input("\nEnter a decimal number: "))

integer_part = int(num)
fractional_part = round(num - integer_part, 2)

print("Integer Part =", integer_part)
print("Fractional Part =", fractional_part)