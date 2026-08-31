class Employee:
    start_time = "10 am"
    end_time = "6 PM"

class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject

t1 = Teacher("Math")
print(t1.subject, t1.start_time, t1.end_time)
        