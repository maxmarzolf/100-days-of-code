import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        guess = input(f'Guess a number between {START} and {END}')
        if not guess:
            raise ValueError('Please enter a number')
        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')
        if guess not in range(START, END+1):
            raise ValueError('Number not in range')
        if guess in self._guesses:
            raise ValueError('Already Guessed')
        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        else:
            high_or_low = 'low' if guess < self._answer else 'high'
            print(f'{guess} is to {high_or_low}')
            return False

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_guesses == 1 and 'guess' or 'guesses'
                print(f'It took you {self.num_guesses} {guess_str}')
                self._win = True
                break
            else:
                print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')


if __name__ == '__main__':
    game = Game()
    game()