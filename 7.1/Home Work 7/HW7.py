# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
def ex1():
    def serch_vowels(list1):
        vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        syllable = []
        for i in list1:
            for j in i:
                count = 0
                for k in j:
                    for l in vowels:
                        if k == l:
                            count += 1
                syllable.append(count)
        if len(set(syllable)) == 1:
            print('Парам пам-пам')
        else:
            print('Пам парам')
    Puh_said = ['пум-порум-пим пара-ра-рам рам-пам-папам па-ра-па-дам'.split()]
    serch_vowels(Puh_said)

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
def ex2():
    def printOperationTable(operation, numRows=6, numColumns=6):
        if operation(1, 1) == 2:
            print(0,end='\t')
        for a in range(1, numRows + 1):
            for b in range(1, numColumns + 1):
                if operation(1, 1) == 2:
                    b = b - 1
                print(operation(a, b), end='\t')
            print()
    print(printOperationTable(lambda x, y: x + y))

# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#  пример  -8 11 0 -23 140 1 => 11 -23
def ex3():
    list1 = list(input('введите ряд цеых чисел через пробел: ').split())
    list1 = list(map(int, list1))
    list2 = list(filter(lambda x: 10 <= abs(x) <= 99, list1))
    print(*list2)

 # Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N, состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано в примере ниже.
def ex4():
    n = int(input('Введите число: '))
    res = map(str,[[i**0*(i == j) for j in range(n)] for i in range(n)])    
    print('\n'.join(res))
ex1()
