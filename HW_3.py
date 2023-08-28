# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 7]
new_list = []

my_set = set(my_list)

for index, value in enumerate(my_set):
    if my_list.count(value) > 1:
        new_list.append(value)

print(new_list)


# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.


my_str = 'Язык программирования — формальный язык, предназначенный для записи компьютерных программ. Язык программирования определяет набор лексических, синтаксических и семантических правил, определяющих внешний вид программы и действия, которые выполнит исполнитель под её управлением. Со времени создания первых программируемых машин человечество придумало более восьми тысяч языков программирования. Каждый год их число увеличивается. Некоторыми языками умеет пользоваться только небольшое число их собственных разработчиков, другие становятся известны миллионам людей. Профессиональные программисты могут владеть несколькими языками программирования.'
my_dict = {}

my_str = my_str.lower()
my_str = my_str.replace('.', '')
my_str = my_str.replace(',', '')
my_str = my_str.replace('—', '')

my_str_set = set(my_str.split(' '))

for index, value in enumerate(my_str_set):
    if value != '' :
        my_dict.update({value: my_str.count(value)})

sorted_values = sorted(my_dict.values(), reverse=True)
sorted_dict = {}

for i in sorted_values:
    for k in my_dict.keys():
        if my_dict[k] == i and i != 1 and len(sorted_dict) < 10:
            for j in my_dict.keys():
                if my_dict[j] == i:
                    sorted_dict[k] = my_dict[k]
                    break

print(sorted_dict)


# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.

my_equipment = {'tent': 4000, 'torch': 300, 'matches': 100, 'sleeping bag': 1500, 'map': 300, 'compass': 350, 'walking boots': 1000, 'life jacket': 800}
rucksack_weight = 7000

total = sum(my_equipment.values())
difference = total - rucksack_weight

sorted_equipment = sorted(my_equipment.values(), reverse=True)

my_sum = 0
target = []
target_dict = {}

for i in sorted_equipment:
    if (my_sum + i) < rucksack_weight:
        my_sum += i
        target.append(i)

for i in target:
    for k in my_equipment.keys():
        if my_equipment[k] == i:
                    target_dict[k] = my_equipment[k]
                    break
print(my_sum)
print(target_dict)

# Все варианты

import itertools
tables = list(my_equipment.values())
target = rucksack_weight
result = [seq for i in range(len(tables), 0, -1)
          for seq in itertools.combinations(tables, i)
          if sum(seq) <= target]
unique_value = list(set(result))

new_unique_value = ''

for i in range(len(unique_value)):
    new_unique_value += ' | '
    for j in range(len(unique_value[i])):
        for m in my_equipment.keys():
            if unique_value[i][j] == my_equipment[m]:
                new_unique_value += (str(m) + ' ' + str(my_equipment[m]))
                break
print(new_unique_value)


