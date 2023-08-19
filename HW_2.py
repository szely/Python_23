# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

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


# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата

a = int(input('Введите целое число: '))
b = int(input('Введите основание системы, в которую требуется перевести число: '))
def transfer(a, b):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = ''
    while a > 0:
        res = str(digits[a % b]) + res
        a //= b
    return res

print(transfer(a, b))
print(hex(a))


#  Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
import math
a = str(input('Введите первую дробь: '))
b = str(input('Введите вторую дробь: '))
def calc(a, b):
    a_list = a.split("/")
    b_list = b.split("/")
    sum = str(int(a_list[0]) * int(b_list[1]) + int(a_list[1]) * int(b_list[0])) + "/" + str(int(a_list[1]) * int(b_list[1]))
    mult = str(int(a_list[0]) * int(b_list[0])) + "/" + str(int(a_list[1]) * int(b_list[1]))
    sum_list = sum.split("/")
    div = math.gcd(int(sum_list[0]), int(sum_list[1]))
    sum_1 = str(int(int(sum_list[0]) / div)) + "/" + str(int(int(sum_list[1]) / div))
    answer = 'Сумма дробей: ' + sum_1  +' Произведение дробей: ' + mult
    return answer

print(calc(a, b))

a_list = a.split("/")
b_list = b.split("/")
a1 = Fraction(int(a_list[0]), int(a_list[1]))
b1 = Fraction(int(b_list[0]), int(b_list[1]))
print(a1+b1)
print(a1*b1)