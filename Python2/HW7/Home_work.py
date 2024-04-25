"""
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""


import os

def rename_files(new_name, num_of_digits, start_ext, final_ext, range_name, path='.'):
    count = 1
    for file_name in os.listdir(path):
        if file_name.endswith(start_ext):
            old_name = os.path.splitext(file_name)[0]
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{new_name}{str(count).zfill(num_of_digits)}{final_ext}"
            os.rename(os.path.join(path, file_name), os.path.join(path, new_filename))
            count += 1

rename_files('_new', 2, '.doc', '.md', [0, 3], '.\Files\Texts')