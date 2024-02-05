import random
from brain_games.engine import run_game
from brain_games.consts import GCD_INSTRUCTION


def get_gcd_expression_and_result() -> tuple:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    question = f'{num1} {num2}'
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    result = num1
    return question, str(result)


def run_gcd_game():
    run_game(get_gcd_expression_and_result, GCD_INSTRUCTION)
