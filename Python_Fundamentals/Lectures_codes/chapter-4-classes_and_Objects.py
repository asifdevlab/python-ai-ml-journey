# ============================================
# PYTHON FUNDAMENTALS
# Chapter 4 - Classes And Objects
# Author: Asif Hussain
# ============================================

# Creating a class
class Car: 
    brand = "Toyota"

car1 = Car()
car2 = Car()

print(car1.brand) # Toyota
print(car2.brand) # Toyota


# Constructor in OOP
class Student:
    def __init__(self):
        print("Constructor is called")

stu1 = Student() # "Constructor is called"

# Use of constructor for initializing the values for objects:
class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("Rahul")
stu2 = Student("Asif")

print(stu1.name, stu2.name) # Rahul Asif


