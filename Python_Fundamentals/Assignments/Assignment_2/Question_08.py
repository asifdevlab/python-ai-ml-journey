# Question 8:
# Create a Simple Calculator function: calculator(a, b, operation)
# that performs addition, subtraction, multiplication, or division
# based on the operation parameter (‘+’, ‘-’, ‘*’, ‘/’).

def calculator(a,b,operation):
    if operation == '+':
        return (a + b)
    elif operation == '-':
        return (a - b)
    elif operation == '*':
        return (a * b)
    elif operation == '/':
        return (a / b)

print("Simple Calculator")
num1 = int(input("Enter number first: "))
num2 = int(input("Enter number second: "))

operator = input("Enter the operation to be performed('+' '-' '*' '/'): ")

print(f"{num1} {operator} {num2} = {calculator(num1,num2,operator)}")
