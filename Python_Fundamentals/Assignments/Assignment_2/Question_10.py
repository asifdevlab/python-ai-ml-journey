# Question 10:
# Create a “Number Guessing Game”.
# Given a secret number (decided by you), write a program that asks the user to guess it and prints:
# • "Too high" if the guess is above the number
# • "Too low" if the guess is below the number
# • "Correct!" if the guess matches

secret_number = 19
print("-----Number Guessing Game-----")
print("Try to guess the secret number.")

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break

