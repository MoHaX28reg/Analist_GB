"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

"""

import os
import json
import csv
import pickle

def define_directory(dir_path):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"Родительская директория": root, 
                            "Это": "файл",
                            "Имя": name,
                            "Размер": os.path.getsize(full_path)})
        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"Родительская директория": root, 
                            "Это": "директория",
                            "Имя": name,
                            "Размер": show_file_size(full_path)})
    return results

def show_file_size(path):
    total_size = 0
    for dirpath, dirnames, filename in os.walk(path):
        for f in filename:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def file_json(list_info):
    with open("result.json", "w", encoding='utf-8') as f_json:
        json.dump(define_directory(list_info), f_json, ensure_ascii=False)

def file_csv(list_info):
    with open("result.csv", "w", encoding='utf-8') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=define_directory(list_info)[0].keys())
        writer.writeheader()
        writer.writerows(define_directory(list_info))

def file_pickle(list_info):
    with open("result.pickle", "wb") as f_pickle:
        pickle.dump(define_directory(list_info), f_pickle)

if __name__ == '__main__':
    dir1 = '.\Files'
    file_json(dir1)
    file_csv(dir1)
    file_pickle(dir1)
