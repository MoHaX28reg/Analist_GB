# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def prime_num(a):
    i = 2
    while  i < a:
        if a % i == 0:
            print('Число составное')
            break
        else:
            i += 1
            if i >= a:
                print('Число простое')

x = int(input('Введите число от 1 до 100: '))
if x == 1 or x == 2:
    print('Ну уж проще некуда))')
elif x < 1 or x > 100:
    print('Внимательно читай условия')
else: prime_num(x)