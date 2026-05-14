# ============================================
# CONDITIONAL STATEMENTS IN PYTHON
# Chapter 2 - Decision Making
# Author: Asif Hussain
# ============================================


# --------------------------------------------
# IF-ELSE STATEMENT
# --------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
    print("You can drive")

else:
    print("You can't vote")


# --------------------------------------------
# ELIF STATEMENT - TRAFFIC LIGHT SYSTEM
# --------------------------------------------

color = input("\nEnter traffic light color: ")

if color.lower() == "red":
    print("Stop")

elif color.lower() == "green":
    print("Go")

elif color.lower() == "yellow":
    print("Look")

else:
    print("Invalid traffic light color")


# --------------------------------------------
# ELIF STATEMENT - AGE CATEGORY
# --------------------------------------------

age = int(input("\nEnter your age: "))

if age < 13:
    print("Child")

elif age >= 13 and age < 18:
    print("Teenager")

else:
    print("Adult")


# --------------------------------------------
# LOGIN SYSTEM USING IF-ELIF
# --------------------------------------------

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("Access Granted")

elif username != "admin":
    print("Incorrect Username")

else:
    print("Wrong Password")


# --------------------------------------------
# MULTIPLE OF FIVE CHECK
# --------------------------------------------

number = int(input("\nEnter a number: "))

if number % 5 == 0:
    print("Multiple of Five")

else:
    print("Not a Multiple of Five")


# --------------------------------------------
# ODD-EVEN CHECK
# --------------------------------------------

num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("EVEN")

else:
    print("ODD")


# --------------------------------------------
# NESTED IF STATEMENT
# --------------------------------------------

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("Login Successful")

else:
    if username != "admin":
        print("Wrong Username")

    else:
        print("Wrong Password")


# --------------------------------------------
# MATCH CASE STATEMENT
# --------------------------------------------

color = input("\nEnter traffic light color: ")

match color.lower():

    case "green":
        print("Go")

    case "yellow":
        print("Look")

    case "red":
        print("Stop")

    case _:
        print("Invalid Color")