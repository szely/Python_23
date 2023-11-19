# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, surname, father_name, age, sex):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self._age =age
        self.sex = sex
    def birthday(self):
        self._age += 1
    def full_name(self):
        return (f' ФИО = {self.surname} {self.name} {self.father_name} Пол = {self.sex} Возраст =  {self._age}')


p1 = Person('Сергей', 'Зеленин', 'Викторович', 30, 'Муж')
p2 = Person('Андрей', 'Иванов', 'Иванович', 11, 'Муж')

print(p1.full_name())
print(p2.full_name())
p1.birthday()
print(p1.full_name())
print(p2._age)
