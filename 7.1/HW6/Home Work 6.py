# Задача №45. 
# Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

def serch_div(number):
    arr = [1]
    for div in range(2,int(number**0.5)+1):
        if div*div == number:
            arr.append(div)
        elif number % div == 0:
            arr += [div,number//div]
    return arr
def ex1():
    n = int(input("Введите число n: "))
    arr = {}
    for i in range(1, n):
        for j in range(1, n):
            divi = serch_div(i)
            divj = serch_div(j)
            if sum(divi) == j and sum(divj) == i and i != j and i < j:
                print(f'{i} {j}')

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def ex2():
    a1 = int(input('Введите первый элемент прогрессии: '))
    n = int(input("Введите колличество элементов: "))
    d = int(input('Введите разность элементов: '))
    ar_progr = []
    an = 0
    for i in range(1, n + 1):
        an = a1 + d * (i - 1)
        ar_progr.append(an)
    print(ar_progr)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
def ex3():
    min = int(input('Введите заданный миимум: '))
    max = int(input('Введите заданный максимум: '))
    a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    for i in range(len(a)):
        if min <= a[i] <= max:
            print(i, end=' ')

ex1()