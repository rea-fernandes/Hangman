# 🎮 Hangman Game

A simple **single-player Hangman game written in Python**.

Hangman is a classic word-guessing game. The computer randomly selects a word, and you have to guess the letters before the hangman is completed.

## ✨ Features

- 🎲 Randomly generated words
- 👤 Single-player gameplay
- 🔤 Letter-by-letter guessing
- 💀 ASCII hangman that progresses with each wrong guess
- ❌ Maximum of 6 wrong guesses
- 🌐 Uses an online API to get random words

## 🖥️ Example

```text
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========

Word: p _ t h _ n

Wrong guesses: 2/6

Guess a letter:
````

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/rea-fernandes/Hangman.git
cd hangman
```

### 2. Install the required package

```bash
pip install -r requirements.txt
```

### 3. Run the game

```bash
python hangman.py
```

## 🎯 How to Play

1. Start the game.
2. The computer chooses a random word.
3. Guess one letter at a time.
4. If your guess is correct, the letter appears in the word.
5. If your guess is wrong, another part of the hangman is drawn.
6. Guess the entire word before reaching 6 wrong guesses to win!

## 📦 Requirements

* Python 3.x
* `requests`

## 📁 Project Structure

```text
hangman/
├── hangman.py
├── requirements.txt
└── README.md
```

## 🔮 Future Improvements

Some ideas for future versions:

* [ ] Add difficulty levels
* [ ] Add a score system
* [ ] Add categories for words
* [ ] Add colored terminal output
* [ ] Add replay functionality
* [ ] Add a larger word API
