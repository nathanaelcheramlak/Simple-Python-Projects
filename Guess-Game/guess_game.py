from utils.NumberGenerator import generate_random_number
from utils.InputValidation import authentication, command_checker

def main():
    command = 3
    while command_checker(command) != 4:
        print('''
        Guess Game V 1.0 by Nathanael
            1. Start!
            2. How to Play
            3. About
            4. Quit
        ''')
        command = int(input("----> "))
        if command == 1:
            guess_list = []
            generated_number = generate_random_number()
            while guess_list != generated_number:
                guess = input('Enter Numbers: ')
                auth = authentication(guess)
                guess_list = []
                num_count = 0
                position = 0
                if auth:
                    for i in guess:
                        guess_list.append(i)
                    for i in guess_list:
                        if i in generated_number:
                            num_count += 1

                    for idx, val in enumerate(guess_list):
                        if val == generated_number[idx]:
                            position += 1
                    print('Position:', position, 'and Number:', num_count)
                else:
                    print('Invalid Input!')
            else:
                print("\033[92mCongratulations! You Won\033[0m")
                play_again = input("Do you want to play again? y/n")
                if play_again.lower() == 'n':
                    break
        elif command == 2:
            print(
                """
Guess The Number is a game where you must use your logic in order to guess a 4-digit secret
number selected by the computer at the beginning of the game. The number is formed with 
digits from \033[92m1 to 9\033[0m each digit appears once at most.

This number is guessed by you via multiple attempts.
An attempt consists in a proposed number, selected by you, and the computer's reply.
The computer must tell you, in his reply, how many digits have you guessed on the same position,
and how many digits have you guessed on a different position.

Using information from the computer's reply,
you must guess the number using as few moves as possible. Good luck!
                """
            )
        elif command == 3:
            print("Guess Game V1.0\nMade by Nathanael Cheramlak")
        elif command == 4:
            print("\033[92mQuitted Successfully\033[0m")

    print("Thanks for Playing!")

if __name__ == "__main__":
    main()
