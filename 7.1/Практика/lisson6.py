# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
import random

def ex1():
    a = sorted(list(random.randint(1, 9) for _ in range(10)))
    print(a)    
    count_2 = list(set(a))
    count_3 = 0
    print(count_2)
    for i in range(len(count_2)):
        count_1 = 0
        for j in range(len(a)):            
            if count_2[i] == a[j]:
                count_1 += 1
        if count_1 > 1:
            count_3 += count_1
    print(count_3)


# def ex2():
#     def find_divs(number):
#     lst = [1]
#     for div in range(2,int(number**0.5)+1):
#         if div*div == number:
#             lst.append(div)
#         elif number % div == 0:
#             lst += [div,number//div]
#     return lst
#     n = int(input("Введите число n: "))
#     m = int(input('Введите число m: '))
#     divs = find_divs(n)
#     print(sum(divs) == m)


ex1()
