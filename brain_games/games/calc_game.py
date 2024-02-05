import random
from brain_games.consts import MATH_SIGNS


CALC_INSTRUCTION = 'What is the result of the expression?'


def get_math_expression_and_result() -> tuple:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_action = random.choice(MATH_SIGNS)
    question = f'{num1} {math_action} {num2}'
    match math_action:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2

    return question, str(result)


gamefunc = get_math_expression_and_result
instruction = CALC_INSTRUCTION
