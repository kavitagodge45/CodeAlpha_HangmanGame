import random

words = ["apple", "tiger", "chair", "robot", "plant"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:
    display_word = ""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("\nWord:", display_word)
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print(f"Wrong! Attempts left: {max_attempts - wrong_guesses}")

    if "_" not in display_word:
        print("\n You Won! The word was:", word)
        break

if wrong_guesses == max_attempts:
    print("\n You Lost! The word was:", word)