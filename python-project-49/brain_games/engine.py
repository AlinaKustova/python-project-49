import prompt


def description_and_comprasion(task):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    rounds = 3

    for _ in range(rounds):
        question, correct_answer = task()
        print('Question: ' + question)

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(." +
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")