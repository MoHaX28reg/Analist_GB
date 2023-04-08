# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите тёхзначное число: '))
sum = 0

if 100 < number < 999:
    while number >= 1:
      sum += int(number % 10)
      number /= 10
    print(sum)
else:
   print('Число не соответствует условию задачи')


