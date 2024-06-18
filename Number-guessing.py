import random

# Set the secret number
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    # Ask the user for their guess
    user_guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(" Congratulations! You guessed the number in {attempts} attempts.")
        break

    # Check if the user's guess is too high or too low
    elif user_guess > secret_number:
        print("Your guess is too high. Try again!")
    else:
        print("Your guess is too low. Try again!")

print("Thanks for playing!")