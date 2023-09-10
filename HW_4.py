# ✔ Напишите функцию для транспонирования матрицы

N = 2
M = 3
A = []
count = 0

for i in range(N):
    A.append([0]*M)
for i in range(N):
    for j in range(M):
         A[i][j] = count
         count += 1
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()

print_matrix(A)
def trans (matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([0] * len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix
print()
print_matrix(trans(A))

# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

a = 1
b = 2
c = 3
d = 4
c = 4
def get_dict(*args):
    my_dict = {}
    for i in args:
        my_dict[i] = hex(i)
    return my_dict

print(get_dict(a, b, c, d, c))

# ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

account_balance = 0
COMISSION_PERSENTAGE = 0.015
COMISSION_LOWER_LIMIT = 30
COMISSION_UPPER_LIMIT = 600
INCOME_PERSENTAGE = 0.03
LIMIT_FOR_TAX = 5_000_000
TAX = 0.1
count_transaction = 0
def account(account_balance,  action, sum):
    income = 0
    if account_balance > LIMIT_FOR_TAX:
        account_balance = account_balance * (1-TAX)
    if count_transaction % 4 == 0:
        income = account_balance * INCOME_PERSENTAGE
    if sum > 0 and action == 'снять':
        if sum * COMISSION_PERSENTAGE < COMISSION_LOWER_LIMIT:
            commission = COMISSION_LOWER_LIMIT
        elif sum * COMISSION_PERSENTAGE > COMISSION_UPPER_LIMIT:
            commission = COMISSION_UPPER_LIMIT
        else:
            commission = sum * COMISSION_PERSENTAGE
        if (account_balance - (sum + commission)) < 0:
            account_balance = account_balance
        else:
            account_balance = account_balance - sum - commission + income
    elif sum > 0 and action == 'внести':
        account_balance = account_balance + sum + income
    return account_balance

print(f'Здравстуйте! Текущий остаток на счете {account_balance}.')
action = str(input('Что Вы хотите сделать? "снять/внести/выйти": '))

while action != 'выйти':
    count_transaction += 1
    sum = int(input(f'Сколько Вы хотите {action}? Введите сумму кратную 50: '))
    if sum % 50 == 0:
        account_balance = account(account_balance, action, sum)
        print(f'Остаток: {float(account_balance)}')
        action = str(input('Что Вы хотите сделать? "снять/внести/выйти": '))
    else:
        print('Введите сумму кратную 50!')