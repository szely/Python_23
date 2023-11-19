# Напишите для задачи 1 тесты unittest
# ● возврат строки без изменений
# ● возврат строки с преобразованием регистра без потери символов
# ● возврат строки с удалением знаков пунктуации
# ● возврат строки с удалением букв других алфавитов
# ● возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest


def func_clear_text(text: str) -> str:
    new_text = ''
    for letter in text:
        if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90 or letter == ' ':
            new_text += letter
    return new_text.lower()


class TestString(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual('hello world', func_clear_text('hello world'), msg='All is not Ok')

    def test_no_lower(self):
        self.assertEqual('hello world', func_clear_text('Hello world'), msg='All is not Ok')

    def test_no_punct(self):
        self.assertEqual('hello world', func_clear_text('hello world,'), msg='All is not Ok')

    def test_no_rissian(self):
        self.assertEqual('hello world', func_clear_text('Hello worldПривет'), msg='All is not Ok')

    def test_no_all(self):
        self.assertEqual('hello world', func_clear_text('Hello, world_Привет'), msg='All is not Ok')


if __name__ == '__main__':
    unittest.main(verbosity=2)