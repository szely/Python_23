# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

this_way = '/Users/a1234/Yandex.Disk.localized/Документы/ОБУЧЕНИЕ/GB/1. Введение в программирование/2/Урок 2. Базовые алгоритмы и массив как структура данных - Исправлено.docx'

def find_file (my_way):
    file_ext_name = my_way.split('/')[-1]
    way_name = my_way[:-len(file_ext_name)]
    ext_name = file_ext_name.split('.')[-1]
    file_name = file_ext_name.replace(ext_name, '')[:-1]
    info_file = (way_name, file_name, ext_name)
    return info_file

print(find_file(this_way))


# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

my_name = ['Ivan', 'Sergei', 'Nicolay']
my_salary = [100_000, 150_000, 200_000]
my_rate = ['30.20%', '25.15%', '45.10%']

my_gen = {i: my_salary[my_name.index(i)] * float(my_rate[my_name.index(i)].replace('%','')) / 100 for i in my_name}
print(my_gen)

# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

n = 10
def fibo(n):
    fib1 = 1
    fib2 = 1
    yield fib1
    yield fib2
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
        yield fib2

print(*fibo(n))

for num in fibo(n):
    print(num)
