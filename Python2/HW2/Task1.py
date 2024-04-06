# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input("Введите число: "))

x = hex(num)[2:]
 
string_fin = ''
str_16 = '0123456789ABCDEF'
 
while num > 0:
    string_fin = str_16[num % 16] + string_fin
    num //= 16
 
print(string_fin)
print(x)

