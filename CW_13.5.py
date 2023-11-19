# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import json

from MYEXP import LevelExeption, AccessExeption


class User:

    def __init__(self, name, level, user_id):
        self.name = name
        self.level = level
        self.user_id = user_id

    def __repr__(self):
        return f'User ({self.name}, {self.user_id}, {self.level})'

class ProjectUser:

    def __init__(self):
        self.user_set = set()

    def my_json(self):
        with open('new_file.json', 'r', encoding='utf=8') as f:
            my_dict = json.load(f)
        for level, value in my_dict.items():
            for user_id, name in value.items():
                new_user = User(name, user_id, level)
                self.user_set.add(new_user)
        return self.user_set

u1 = ProjectUser()
print(u1.my_json())
