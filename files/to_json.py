import random as rnd
# def func_sum(file1, file2):
#     with (
#         open(file1, 'r', encoding='utf-8') as f1,
#         open(file2, 'r', encoding='utf-8') as f2,
#         open('res.txt','w', encoding='utf-8') as res):
#         digit = f1.readlines()
#         name = f2.readlines()
#         max_len = max(len(digit), len(name))
#         min_len = min(len(digit), len(name))
#         rate = max_len// min_len
#         rate2 = max_len % min_len
#         if len(digit) > len(name):
#             name *= rate
#             name += name[:rate2]
#         else:
#             digit *= rate
#             digit += digit[:rate2]
#         for i in range(max_len):
#             a = eval(digit[i].replace('|', '*'))
#             b = name[i].replace('\n', '')
#             res.write(f'{b} = {a}\n')
#
# if __name__ == '__main__':
#     func_sum('new_file.txt', 'new_file1.txt')

# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

def my_json(file1):
    