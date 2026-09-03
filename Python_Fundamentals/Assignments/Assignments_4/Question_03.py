# Q3. Create a class Student with private attributes:
#    _name, _roll_no, _marks
#    Provide getter and setter methods with validation:
#    - marks cannot be negative
#    - roll number must be between 1 and 100
#    - name cannot be empty

class Student:
    def __init__(self):
        self._name = ""
        self._roll_no = 0
        self._marks = 0

    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks

    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            print("Error: Name cannot be empty.")

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Error: Roll number must be between 1 and 100.")

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Error: Marks cannot be negative.")

# --- Example usage ---

student2 = Student()
student2.set_name("Aarya Deep")
student2.set_roll_no(1)
student2.set_marks(95)

# student2.set_name("") - this will throw an error

print("Details of student 2:")
print("Name:", student2.get_name())
print("Roll No:", student2.get_roll_no())
print("Marks:", student2.get_marks())



