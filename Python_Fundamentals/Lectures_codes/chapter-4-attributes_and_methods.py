# ============================================
# PYTHON FUNDAMENTALS
# Chapter 4 - Attributes and Methods
# Author: Asif Hussain
# ============================================

#  Class Attributes
class Student: 
    college = "Galgotias College" # class attribute

stu1 = Student()

print(stu1.college)
print(Student.college) # class attribute can also be accessed with class name

# Instance Attributes
class Student:
    def __init__(self, name, gpa): # instance attributes
        self.name = name
        self.gpa = gpa

stu1 = Student("Rahul", 8.7)
print(stu1.name, stu1.gpa)

# Types of Methods
# Instance Methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):      # Instance Method
        print(f"Name: {self.name}, Marks: {self.marks}")

# Class Methods
class Student:
    school_name = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

# Static Methond
class Math:
    @staticmethod
    def add(a,b):
        return a + b


        
        