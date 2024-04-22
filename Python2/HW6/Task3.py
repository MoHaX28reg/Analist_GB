import random
from Task2 import eight_queens

def gen_position():
    pos = list(range(1, 9))
    count = 0
    while count < 4:
        random.shuffle(pos)
        while not eight_queens(pos):
            random.shuffle(pos)
        print(pos)
        count += 1
