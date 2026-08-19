# Question 5:
# Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key ('A', 'B', 'C', 'D')
# depending on the operation they want to perform:
#   A - Add a student
#   B - Update marks
#   C - Search for a student
#   D - Display all students and marks

# Question 5:
# Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key ('A', 'B', 'C', 'D')

student_record = {
    "Asif Hussain": 98,
    "Aarya Deep": 95,
    "Ajay Kumar": 99,
    "Aadya Pathak": 100,
    "Abhishek Yadav": 88
}

print("Initial Student Records:")
print(student_record)
print()

while True:
    print("Select from the options:")
    print("'A' - Add a Student")
    print("'B' - Update marks")
    print("'C' - Search for a student")
    print("'D' - Display all students and marks")
    
    choice = input("\nYour choice: ").upper()
    
    match choice:
        case 'A':
            # Add a new student
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            student_record[name] = marks
            print(f"✓ {name} added with {marks} marks.\n")
            
        case 'B':
            # Update marks
            name = input("Enter student name: ")
            if name in student_record:
                marks = int(input("Enter new marks: "))
                student_record[name] = marks
                print(f"✓ {name}'s marks updated to {marks}.\n")
            else:
                print(f"✗ {name} not found in records.\n")
                
        case 'C':
            # Search for a student
            name = input("Enter student name: ")
            if name in student_record:
                print(f"✓ {name}: {student_record[name]} marks\n")
            else:
                print(f"✗ {name} not found in records.\n")
                
        case 'D':
            # Display all students and marks
            print("\nAll Students and Marks:")
            for name, marks in student_record.items():
                print(f"  {name}: {marks}")
            print()
            
        case _:
            print("✗ Invalid choice. Please try again.\n")
    
    again = input("Do you want to continue? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the system!")
        break