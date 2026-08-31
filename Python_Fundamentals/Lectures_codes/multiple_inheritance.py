class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TeacherAssistant(Teacher,Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name = name

t1 = TeacherAssistant(15_000, 9.8, "Asif")
print(t1.name,t1.salary, t1.gpa)
        