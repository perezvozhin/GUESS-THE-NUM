import random


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def generate_round() -> tuple:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    question = f'{num1} {num2}'
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    result = num1
    return question, str(result)
