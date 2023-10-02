# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.+
# ○ Для каждого объекта укажите файл это или директория. +
# ○ Для файлов сохраните его размер в байтах, а для директорий размер +
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle

directory_way = '/Users/a1234/PycharmProjects/pythonProject_GB/files'

def dr_get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def walk_directory_json(directory_way):
    os.chdir(directory_way)
    my_dict = {"Directory": {}, "Files": {}}
    data = list(os.walk(os.getcwd()))
    for i in data:
        parent = i[0].split('/')[-1]
        my_dict["Directory"][parent] = {}
        for j in i[1]:
            y = dr_get_size(os.path.abspath(j))
            my_dict["Directory"][parent][j] = str(y)
    for i in data:
        os.chdir(i[0])
        parent = i[0].split('/')[-1]
        my_dict["Files"][parent] = {}
        for u in i[2]:
            q = os.path.getsize(u)
            my_dict["Files"][parent][u] = str(q)
    return my_dict


def walk_directory_csv(directory_way):
    os.chdir(directory_way)
    my_str = '"Type","Parent","Name","Size" \n'
    data = list(os.walk(os.getcwd()))
    for i in data:
        parent = i[0].split('/')[-1]
        for j in i[1]:
            y = dr_get_size(os.path.abspath(j))
            my_str = my_str + '"Directory"' + ',' + f'"{parent}"' + ',' + f'"{j}"' + ',' + f'{y}''\n'
    for i in data:
        os.chdir(i[0])
        parent = i[0].split('/')[-1]
        for u in i[2]:
            q = os.path.getsize(u)
            my_str = my_str + '"Files"' + ',' + f'"{parent}"' + ',' + f'"{u}"' + ',' + f'{q}''\n'
    return my_str

my_dict = walk_directory_json(directory_way)
os.chdir(directory_way)
with open('new_file3.json', 'w', encoding='utf=8') as f:
    json.dump(my_dict, f, indent=2)


my_str = walk_directory_csv(directory_way)
os.chdir(directory_way)
with open('new_file.csv', 'w', encoding='utf-8') as f_write:
    f_write.write(my_str)


with open('new_file.pickle', 'wb') as f:
    pickle.dump(my_dict, f)