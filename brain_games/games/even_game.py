import random


def is_even(num):
    return num % 2 == 0


instruction = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_game() -> tuple:
    num = random.randint(1, 100)
    if is_even(num):
        answer = "yes"
    else:
        answer = "no"
    return num, answer
