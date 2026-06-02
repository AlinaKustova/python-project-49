from random import randint

from brain_games.engine import description_and_comprasion


def create_sequence(start_number, hidden_position, length, step):
    row = []

    for index in range(0, length):
        current_elem = start_number + index * step

        if index == hidden_position - 1:
            row.append('..')
            hidden_elem = current_elem
        
        else:
            row.append(str(current_elem))
    
    return row, hidden_elem


def play():
    start_number = randint(1, 100)
    length_sequence = randint(5, 15)
    hidden_number_position = randint(1, length_sequence)
    step = randint(1, 10)
    
    sequence_row, correct_answer = create_sequence(start_number,
                        hidden_number_position, length_sequence, step)

    question = f'{' '.join(sequence_row)}'

    return question, str(correct_answer)


def main():
    description = 'What number is missing in the progression?'
    
    description_and_comprasion(play, description)


if __name__ == "__main__":
    main()