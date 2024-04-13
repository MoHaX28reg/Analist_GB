#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

start_lst = [1, 8, 4, 3, 1, 7, 1, 3, 7, 2, 9, 0, 4]
lst_doob = []
final_lst = []
for item in start_lst:
    if item not in lst_doob:
        if start_lst.count(item) > 1:
            lst_doob.append(item)
    if item not in final_lst:
        final_lst.append(item)

print(f'Дублирующиеся элементы: {lst_doob}')
print(f'Список без дубликатов: {final_lst}')