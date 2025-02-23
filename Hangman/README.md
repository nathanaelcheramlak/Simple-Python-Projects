# Hangman Game

A simple command-line Hangman game implemented in Python. This project randomly selects a word from a predefined list and allows the user to guess letters until they either guess the word correctly or run out of lives.

## Features

- Random word selection from a predefined list
- Visual representation of remaining lives
- Case-insensitive letter input
- Tracks correct and incorrect guesses
- Ends game when the word is guessed or all lives are lost

## How to Play

1. Run the script using Python.
2. The game will display underscores representing the letters in the word.
3. Guess one letter at a time by typing and pressing Enter.
4. If the letter is in the word, it will be revealed.
5. If the letter is incorrect, you lose a life.
6. The game ends when you either guess the word correctly or lose all lives.

## Installation

Ensure you have Python installed on your system.

1. Clone this repository:
   ```sh
   git clone https://github.com/nathanaelcheramlak/Python-Games.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Python-Games/Hangman
   ```
3. Run the script:
   ```sh
   python hangman.py
   ```

## Example Usage

```
Welcome to Hangman
 _ _ _ _ _
Guess: e
Correct! e is in the word.

Guess: x
Wrong x is not in the word.

You Won! apple is the word.
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributions

Feel free to submit issues or pull requests to improve the Hangman game!

## Author

[Nathanael Cheramlak](https://github.com/nathanaelcheramlak)
