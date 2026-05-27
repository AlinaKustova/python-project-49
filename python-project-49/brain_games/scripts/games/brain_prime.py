from random import randint

from brain_games.engine import description_and_comprasion


def is_prime(number):
    if number == 1:
        return False
    
    else:
        for num in range(2, round(number ** 0.5) + 1):
            if number % num == 0:
                return False
    
    return True
    

def play():
    number = randint(1, 100)

    number_is_prime = is_prime(number)
    correct_answer = 'yes' if number_is_prime else 'no'

    return str(number), correct_answer


def main():
    description = 'Answer "yes" if given number is prime.' \
    ' Otherwise answer "no".'

    description_and_comprasion(play, description)


if __name__ == "__main__":
    main()