from random import randint
import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
    return name

def is_even(number):
    return True if number % 2 == 0 else False

def play():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    name = welcome_user()

    for _ in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ')

        number_is_even = is_even(number)
        even = 'yes' if number_is_even else 'no'

        if answer == even:
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play()

if __name__ == "__main__":
    main()