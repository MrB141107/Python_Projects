import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]

# Function to select a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to initialize the game
def initialize(word):
    display = ["_"] * len(word)
    incorrect_guesses = []
    return display, incorrect_guesses

# Function to display the current state of the game
def display_game(display, incorrect_guesses):
    print("Word: " + " ".join(display))
    print("Incorrect guesses: " + " ".join(incorrect_guesses))

# Function to play the game
def play_hangman():
    word = choose_word()
    display, incorrect_guesses = initialize(word)
    attempts = 6  # Number of allowed incorrect guesses

    while True:
        display_game(display, incorrect_guesses)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            incorrect_guesses.append(guess)
            attempts -= 1

        if "_" not in display:
            print("Congratulations! You guessed the word: " + word)
            break

        if attempts == 0:
            print("You ran out of attempts. The word was: " + word)
            break

# Start the game
print("Welcome to Hangman!")
play_hangman()
