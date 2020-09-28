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
    print(opponents_choice)


if __name__ == '__main__':
    main()