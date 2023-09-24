# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.M.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

CHECK_YEAR = [1, 9999]
DATA_DATES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
FLOAT_MONTH = 2
def ch_date(date):
    list_dates = date.split('.')
    year = int(list_dates[2])
    month = int(list_dates[1])
    day = int(list_dates[0])
    answer = False
    if CHECK_YEAR[0] <= year <= CHECK_YEAR[1]:
        if month in DATA_DATES.keys():
            if day <= DATA_DATES[month]:
                answer = True
            elif month == FLOAT_MONTH and day <= DATA_DATES[month] + 1 and ch_year(year) == True:
                answer = True
    return answer
def ch_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True


