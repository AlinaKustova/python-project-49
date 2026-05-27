from random import randint

from brain_games.engine import description_and_comprasion


def is_even(number):
    return number % 2 == 0


def play():
    number = randint(1, 100)

    number_is_even = is_even(number)
    correct_answer = 'yes' if number_is_even else 'no'

    return str(number), correct_answer


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'

    description_and_comprasion(play, description)


if __name__ == "__main__":
    main()