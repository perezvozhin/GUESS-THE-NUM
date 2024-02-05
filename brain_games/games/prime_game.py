import random
from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_num_and_prime_answer() -> tuple:
    number = random.randint(1, 100)
    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"

    return number, answer


def run_prime_game():
    run_game(get_num_and_prime_answer, PRIME_INSTRUCTION)
