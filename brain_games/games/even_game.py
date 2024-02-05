import random


def is_even(num):
    return num % 2 == 0


EVEN_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_num_and_even_ans() -> tuple:
    num = random.randint(1, 100)
    if is_even(num):
        answer = "yes"
    else:
        answer = "no"
    return num, answer


gamefunc = get_num_and_even_ans
instruction = EVEN_INSTRUCTION
