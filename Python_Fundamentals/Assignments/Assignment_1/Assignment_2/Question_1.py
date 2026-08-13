# Question 1:
# Write a program that takes salary as input.
# Using conditional statements, calculate the final tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary = int(input("Enter your salary: "))

final_tax_rate = 0
if salary < 30000:
    final_tax_rate = (5/100) * salary
elif 30000 <= salary < 70000:
    final_tax_rate = (15/100) * salary
elif salary >= 70000:
    final_tax_rate = (25/100) * salary

print(f"Final tax rate of the salary is {final_tax_rate}")