# Решить задания, которые не успели решить на семинаре.
# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" "Зачет" ставится,
# если Слушатель успешно выполнил задание. "Незачет" ставится, если Слушатель не выполнил задание.
# Критерии оценивания: 1 - Слушатель написал корректный код для задачи, добавил к ним логирование ошибок и полезной информации.

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.M.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import logging
import argparse


CHECK_YEAR = [1, 9999]
DATA_DATES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
FLOAT_MONTH = 2
def ch_date(date):
    list_dates = date.split('.')
    year = int(list_dates[2])
    month = int(list_dates[1])
    day = int(list_dates[0])
    my_answer = False
    if CHECK_YEAR[0] <= year <= CHECK_YEAR[1]:
        if month in DATA_DATES.keys():
            if day <= DATA_DATES[month]:
                my_answer = True
            elif month == FLOAT_MONTH and day <= DATA_DATES[month] + 1 and ch_year(year) == True:
                my_answer = True
    if my_answer:
        logger.info(f'{date} = {my_answer}')
    else:
        logger.error(f'{date} = {my_answer}')
    return my_answer

def ch_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return False
    else:
        logger.info(f'Leap {year}')
        return True


if __name__ == '__main__':
    FORMAT = '{levelname: <8}, {asctime}, {name}, {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='my_log_ch.log', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    my_date = ['30.02.2020', '28.402.2010', '29.02.2020', '31.12.2020', '33.12.2023', '29.02.2023', '29.02.2024']
    for i in my_date:
        print(i, ch_date(i), end=' | ')
    print()
    parser = argparse.ArgumentParser(description='My first argumentparser')
    parser.add_argument('date', metavar='date', type=str, nargs='?', help='press date')
    args = parser.parse_args()
    print(args.date, ch_date(args.date))

# python3 HW_15_1.py '30.22.2020'
