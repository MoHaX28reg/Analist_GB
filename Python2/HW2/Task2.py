# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions


str_a = '1/7'
str_b = '31/59'

def string_to_int(x, y):
    lst_x = x.split('/')
    lst_y = y.split('/')
    x1 = int(lst_x[0])
    x2 = int(lst_x[1])
    y1 = int(lst_y[0])
    y2 = int(lst_y[1])
    print(f'Умножение дробей: {x1 * y1}/{x2 * y2}')
    print(f'Сложение дробей: {(x1 * y2) + (y1 * x2)}/{x2 * y2}')

string_to_int(str_a, str_b)
