from random import randint

from brain_games.engine import description_and_comprasion


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a


def play():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)

    question = f'{number_1} {number_2}'
    correct_answer = gcd(number_1, number_2)

    return question, str(correct_answer)


def main():
    description = 'Find the greatest common divisor of given numbers.'
    
    description_and_comprasion(play, description)


if __name__ == "__main__":
    main()