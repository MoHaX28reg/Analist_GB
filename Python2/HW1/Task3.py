# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки.

import random

x_num = random.randint(1, 1000)

x_player = int(input("Попробуёте угадать число: "))

count = 1
if x_player == x_num:
    print("Вот это удача, с первого раза угадал")
else:
    while x_num != x_player:
        if x_num > x_player:
            x_player = int(input("Не-а, нужно больше. Давай ещё раз: "))
            count += 1
        else: 
            x_num < x_player
            x_player = int(input("Не угадал, давай меньше. Давай ещё раз: "))
            count += 1
    print(f'Ура, ты угадал. Число попыток: {count}')