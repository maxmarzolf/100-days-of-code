import random


class Computer:
    def __init__(self, choice):
        self.choice = choice

    def choose_state(self):
        possible_states = ['rock', 'paper', 'scissors']
        self.choice = random.choice(possible_states)
        return self.choice


def main():
    start_game()


def start_game():
    opponent = Computer('')
    opponents_choice = opponent.choose_state()
    player = players_choice()
    determine_winner(opponents_choice, player)


def players_choice():
    choice = input()
    return choice


def determine_winner(opponent, player):
    print('computer chose ' + opponent)
    if opponent == 'rock' and player == 'scissors':
        print('you loose - rock smashes scissors')
    if opponent == 'paper' and player == 'rock':
        print('you loose - paper covers rock')
    if opponent == 'scissors' and player == 'paper':
        print('you loose - scissors cuts paper')

    if opponent == 'rock' and player == 'paper':
        print('you win - paper covers rock')
    if opponent == 'paper' and player == 'scissors':
        print('you win - scissors cuts paper')
    if opponent == 'scissors' and player == 'rock':
        print('you win - rock smashes scissors')

    if opponent == 'rock' and player == 'rock':
        print('tie')
    if opponent == 'paper' and player == 'paper':
        print('tie')
    if opponent == 'scissors' and player == '=scissors':
        print('tie')


if __name__ == '__main__':
    main()
