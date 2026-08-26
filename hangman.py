import requests

# Get a random word from the internet
response = requests.get("https://random-word-api.herokuapp.com/word")
word = response.json()[0].lower()

guessed_letters = set()
wrong_guesses = 0
max_wrong = 6

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    """
]

while wrong_guesses < max_wrong:

    # Print hangman
    print(hangman[wrong_guesses])

    # Print current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")

else:
    print(hangman[wrong_guesses])
    print(f"\n💀 You lost! The word was: {word}")
