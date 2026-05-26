from random import choice, randint

from brain_games.engine import description_and_comprasion


def calculate(number_1, number_2, operation):
    match operation:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case '*':
            return number_1 * number_2


def play():
    print('What is the result of the expression?')
    
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)

    operation = choice(['+', '-', '*'])
    
    question = f'{number_1} {operation} {number_2}'
    correct_answer = calculate(number_1, number_2, operation)

    return question, str(correct_answer)


def main():
    description_and_comprasion(play)


if __name__ == "__main__":
    main()