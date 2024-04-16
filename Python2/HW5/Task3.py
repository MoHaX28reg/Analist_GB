# Создайте функцию генератор чисел Фибоначчи

def fibonacci(x):
    a, b = 0, 1
    count = 0
    while count < x:
        yield a
        a, b = b, a + b
        count += 1

print (*fibonacci(15))