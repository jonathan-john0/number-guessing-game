import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it. Good luck!")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempts!")
            break
        elif guess < number_to_guess:
            print("Too low! 📉")
        else:
            print("Too high! 📈")

        print(f"You have {attempts - attempt} attempts remaining.")

    else:
        print(f"\n Game Over! You've run out of attempts.")
        print(f"The correct number was {number_to_guess}.")

if __name__ == "__main__":
    play_game()