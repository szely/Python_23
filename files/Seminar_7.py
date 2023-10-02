import random as rnd
MIN_NUMBER = -1000
MAX_NUMBER = 1000

def fun_gen(num_str: int, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            int_num = rnd.randint(MIN_NUMBER, MAX_NUMBER)
            float_num = rnd.uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{int_num}|{float_num:.2f}\n')

if __name__ =='__main__':
    fun_gen(5, 'new_file.txt')

def func_sum(file1, file2):
    with (
        open(file1, 'r', encoding='utf-8') as f1,
        open(file2, 'r', encoding='utf-8') as f2,
        open('res.txt', 'w', encoding='utf-8') as res):
        digit = f1.readlines()
        name = f2.readlines()
        max_len = max(len(digit), len(name))
        min_len = min(len(digit), len(name))
        rate = max_len// min_len
        rate2 = max_len % min_len
        if len(digit) > len(name):
            name *= rate
            name += name[:rate2]
        else:
            digit *= rate
            digit += digit[:rate2]
        for i in range(max_len):
            a = eval(digit[i].replace('|', '*'))
            b = name[i].replace('\n', '')
            res.write(f'{b} = {a}\n')

if __name__ == '__main__':
    func_sum('new_file.txt', 'new_file1.txt')