# Question 7:
# Design a program to continuously input a number n from user
# and print if it is positive or negative until the user enters "Quit".

while True:
    user_input = input("Enter a number (or type 'Quit' to exit): ")

    if user_input == "Quit":
        break

    num = int(user_input)
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

