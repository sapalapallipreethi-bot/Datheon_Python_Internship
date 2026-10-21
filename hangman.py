
import random

words = ["PYTHON", "COMPUTER", "DEVELOPER", "PROGRAM", "SCIENCE"]
secret_word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

stages = [
    "  +---+\n  |   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n========="
]

print("WELCOME TO HANGMAN!")
print("Guess the hidden word, one letter at a time.")

while wrong_guesses < max_attempts:
    print("\n" + stages[wrong_guesses])

    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", display)
    print("Guessed letters:", sorted(guessed_letters))
    print("Attempts remaining:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        print("The word was:", secret_word)
        break

    guess = input("Enter one letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\n" + stages[max_attempts])
    print("Game over! The word was:", secret_word)

print("Thanks for playing!")
