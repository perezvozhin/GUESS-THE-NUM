import random

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    gcd = x
    return str(gcd)


def generate_round() -> tuple:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    question = f'{num1} {num2}'
    result = find_gcd(num1, num2)
    return question, result
