import random

# List of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Randomly select a word
word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

# Hide the word with underscores
display_word = ["_"] * len(word)

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses available.")

# Main game loop
while incorrect_guesses < max_incorrect_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("Good guess!")

        # Reveal the correct letter
        for index in range(len(word)):
            if word[index] == guess:
                display_word[index] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print(
            "Incorrect guesses:",
            incorrect_guesses,
            "/",
            max_incorrect_guesses
        )

# Check the result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n❌ Game Over!")
    print("The word was:", word)

print("\nThanks for playing Hangman!")