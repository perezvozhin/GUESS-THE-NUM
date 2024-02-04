import random
from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans() -> tuple:
    num = random.randint(1, 100)
    if is_even(num):
        answer = "yes"
    else:
        answer = "no"

    return num, answer


def run_even_game():
    run_game(get_num_and_even_ans, EVEN_INSTRUCTION)
