import random


GCD_INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_gcd_expression_and_result() -> tuple:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    question = f'{num1} {num2}'
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    result = num1
    return question, str(result)


gamefunc = get_gcd_expression_and_result
instruction = GCD_INSTRUCTION
