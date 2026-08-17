# ============================================
# PYTHON FUNDAMENTALS
# Chapter 3 - DICTIONARY
# Author: Asif Hussain
# ============================================

# Dictionary Creation
my_dict = {
    "Name" : "Asif",
    "Age" : 22,
    "City" : "Gopalganj"
}
print(my_dict)

# Accessing Values (using key & [])
student = {"Name": "Aarya", "Age": 19}
print(student["Age"]) # 19

# Dictionary Methods
# keys() - return all keys
# values() - returns all values
# items() - returns key-value pairs as tuples
# get(key) - another way to access value if it does'nt exist it returns None.
# update(new_item) - add a new item to the dictionary

d = {
    "Name": "Asif Hussain",
    "Subjects": ["Maths", "Science", "English"],
    "CGPA": 9.8
}

print(d.keys()) # dict_keys
print(d.values()) # dict_values
print(d.items()) # dict_items

print(d.get("SGPA")) # return None as no such key present in the dictionary

new_item = {"State": "Bihar"}
d.update(new_item)
print(d)

# Loops on Dictionary
d = {
    "Name": "Asif Hussain",
    "Subject": ["Maths", "Science", "English"],
    "CGPA": 9.5
}

for key, value in d.items():
    print(key, value)
