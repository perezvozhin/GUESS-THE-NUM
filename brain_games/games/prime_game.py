import random


PRIME_INSTRUCTION = ('Answer "yes" if given number is prime. Otherwise answer '
                     '"no".')


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


gamefunc = get_num_and_prime_answer
instruction = PRIME_INSTRUCTION
