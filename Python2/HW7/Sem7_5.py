"""
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""
from Analist.Python2.HW7.Sem7_4 import generate_files

def generate_with_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        generate_files(key, 'files', num_files=value)


if __name__ == '__main__':
    d = {
        'doc': 5,
        'jpg': 5,
        'png': 5,
        'txt': 5,
    }
    generate_with_dictionary(d)
