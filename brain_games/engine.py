import prompt


AMOUNT_OF_ROUNDS = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string(empty=True, prompt="May I have your name? ")
    print(f'Hello, {name}!\n'
          f'{game.instruction}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = game.start_game()
        print(f'Question: {question}')
        user_answer = prompt.string(empty=True, prompt='Your answer: ')
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer is {correct_answer}.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
