import prompt
from brain_games.consts import AMOUNT_OF_ROUNDS


def run_game(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string(empty=True, prompt="May I have your name? ")
    print(f'Hello, {name}!\n'
          f'{game_module.instruction}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = game_module.gamefunc()
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
