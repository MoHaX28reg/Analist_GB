# Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г. Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190. Известно, что их веса распределены нормально. Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест.)

m = 200
n = 10
x = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
tkp = 3.24
sum = 0
for i in x:
    sum = sum + i
xcp = sum / n

sum2 = 0
for i in x:
    sum2 += (i - xcp) ** 2    


s = (sum2 / (n - 1)) ** (1 / 2)
tp = (xcp - m) * (n ** (1 / 2)) / s

print(tp)
# tp находится в диапазоне tkp (от -1,62 до 1,62), поэтому нулевая теория верна