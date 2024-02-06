import random


instruction = 'What is the result of the expression?'
MATH_SIGNS = '+', '-', '*'


def start_game() -> tuple:
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
