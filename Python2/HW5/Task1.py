# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def file_info(text: str):
    print((os.path.abspath(text), os.path.basename(text), os.path.splitext(text)[1]))


file_info("C:\GB_ucheba\analist\phon.txt")