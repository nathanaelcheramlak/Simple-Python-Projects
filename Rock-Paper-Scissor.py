import random

ALLOWED_CHOICES = ['rock', 'paper', 'scissor']

def get_user_input():
    """Recieves user input until we get a winner."""
    while True:
        user_choice = input('Enter your choice (rock, paper, scissor): ').lower()
        if user_choice in ALLOWED_CHOICES:
            return user_choice
        else:
            print('Invalid input! Please enter one of: rock, paper, scissor')

def determine_winner(user_choice, computer_choice):
    """ Determines the winner of every game. """
    if user_choice == computer_choice:
        return 'Draw!'
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        return 'You Won!'
    else:
        return 'You Lost!'

def main():
    best_of = int(input('Play until how many wins? '))
    computer_wins = 0
    user_wins = 0

    while computer_wins < best_of and user_wins < best_of:
        user_choice = get_user_input()
        computer_choice = random.choice(ALLOWED_CHOICES)
        print(f'Computer chooses {computer_choice}')
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == 'You Won!':
            user_wins += 1
        elif result == 'You Lost!':
            computer_wins += 1

    print("- - - - - - - - - - - - - - ")
    print(f'Final score: You {user_wins} - {computer_wins} Computer')

    if computer_wins > user_wins:
        print("You lost, better luck next time!")
    elif computer_wins < user_wins:
        print("Congratulations, You won!")
    else:
        print("It's a draw!")

