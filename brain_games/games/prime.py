import random

INSTRUCTION = ('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_round() -> tuple:
    number = random.randint(1, 100)
    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"

    return number, answer
