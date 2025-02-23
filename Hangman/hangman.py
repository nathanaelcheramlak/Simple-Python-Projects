from random import choice
from hangman_visuals import lives_visual_dict
from words import word_list

def main():
    LIVES = 7
    word = choice(word_list) # Selects a random word from the list.
    preview_list = list('_' * len(word))
    print("Welcome to Hangman")
    print(lives_visual_dict[LIVES])
    while LIVES > 0:
        guessed_letter = input("Guess: ").lower()
        isThere = False
        for i in range(len(word)):
            if word[i] == guessed_letter:
                preview_list[i] = guessed_letter.upper()
                isThere = True
        if isThere:
            print(f"Correct! {guessed_letter} is in the word.")
            
        else:
            print(f"Wrong {guessed_letter} is not in the word.")
            LIVES -= 1
        if ''.join(preview_list) == word.upper():
            print(f"\n***********\nYou Won! {word} is the word.\n***********")
            break

        print(lives_visual_dict[LIVES])
        print(''.join(preview_list))

    if not LIVES:
        print(f"You Lost! The word was ", word)

if __name__ == "__main__":
    main()