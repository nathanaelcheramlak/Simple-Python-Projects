from random import randint

num = randint(1, 20)
MAX_TRIES = 3

while MAX_TRIES > 0:
    guessed_num = int(input("Guess: "))
    MAX_TRIES -= 1
    if guessed_num < num:
        print('Too Low')
    elif guessed_num > num:
        print('Too High')
    else:
        print("---------\nCorrectly Guessed!\n---------")
        break
if not MAX_TRIES:
    print(f"Out of guesses. But the number was {num}")

print("Thanks for playing.")

