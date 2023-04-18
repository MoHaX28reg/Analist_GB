# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
def ex1():
    n = ('a a a b c a a d c d d')
    m = n.split(' ')
    c = {}
    for i in m:
        if i in c:
            print(f'{i}_{c[i]}', end=' ')
        else: print(i, end=' ')
        c[i] = c.get(i, 0) + 1

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

def ex2():
    text_1 = set('She sells sea shells on the sea shore The shells that she sells are sea shells Im sure.So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells'.split())
    print(len(text_1))

ex1()


