'''
    The goal is to take two mystery numbers, and analyse the following relations:
        1. Greater than
        2. Less than
        3. Greater than or equal to
        4. Less than or equal to
        5. Equal to
        6. Not equal to
'''

import random
def secret_solver(a, b):
    if a > b: print("Number 1 > Number 2 is True")
    else: print("Number 1 > Number 2 is False")

    if a < b: print("Number 1 < Number 2 is True")
    else: print("Number 1 < Number 2 is False")

    if a >= b: print("Number 1 >= Number 2 is True")
    else: print("Number 1 >= Number 2 is False")

    if a <= b: print("Number 1 <= Number 2 is True")
    else: print("Number 1 <= Number 2 is False")

    if a == b: print("Number 1 == Number 2 is True")
    else: print("Number 1 == Number 2 is False")

    if a != b: print("Number 1 != Number 2 is True")
    else: print("Number 1 != Number 2 is False")

if __name__ == "__main__":
    secret_solver(random.randint(1,100), random.randint(1,100))