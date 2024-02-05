import random
from brain_games.consts import (PROGR_LENGTH_MAX, PROGR_LENGTH_MIN)

PROGR_INSTRUCTION = 'What number is missing in the progression?'


def get_progression_and_answer() -> tuple:
    start, step = random.randint(1, 100), random.randint(1, 10)
    progression = []
    progression_length = random.randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)
    for i in range(progression_length):
        progression.append(start + step * i)

    missed_index = random.randint(0, progression_length - 1)
    missed_num = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_num = ' '.join(map(str, progression))

    return progression_with_missed_num, str(missed_num)


gamefunc = get_progression_and_answer
instruction = PROGR_INSTRUCTION
