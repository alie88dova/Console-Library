# -*- coding: utf-8 -*-
import os
from Functional.functions import year_prefix

class Console:
    """
    Отображает в консоли данные с заданными нами настройками
    """
    MAX_LEN = 50

    def menu_wrapper(self):
        text = "   Меню   ".center(self.MAX_LEN, '=') + '\n\n'
        text += "1. Добавить книгу ".center(self.MAX_LEN, ' ') + '\n\n'
        text += "2. Найти книгу ".center(self.MAX_LEN, ' ') + '\n\n'
        text += "3. Удалить книгу ".center(self.MAX_LEN, ' ') + '\n\n'
        text += "4. Вывести все книги ".center(self.MAX_LEN, ' ') + '\n\n'
        text += "5. Взять книгу ".center(self.MAX_LEN, ' ') + '\n\n'
        text += "6. Взять книгу ".center(self.MAX_LEN, ' ') + '\n\n'
        text += "\tДля выбора введите число "
        print(text, end='')
        logic = input()

    def add_wrapper(self):
        text = "   Добавление книги   ".center(self.MAX_LEN, '=') + '\n\n'
        data = {
            "title": "None",
            "author": "None",
            "year": "None",
        }

        question_text = [
            'Введите название книги:',
            'Введите автора произведения (если его нет оставьте пустым)',
            'Введите год издание',
        ]

        keys = list(data.keys())

        for i in range(0, len(keys)):
            print(text)
            print(f"\tНазвание:{data['title']:>{self.MAX_LEN-18}}")
            print(f"\tАвтор:{data['author']:>{self.MAX_LEN - 15 }}")
            print(f"\tГод издания:{year_prefix(data['year']):>{self.MAX_LEN - 21}}\n")
            ans = input(f"{question_text[i]} ")
            data[keys[i]] = ans
            self.clear()
        print(text)
        print(f"\tНазвание:{data['title']:>{self.MAX_LEN - 18}}")
        print(f"\tАвтор:{data['author']:>{self.MAX_LEN - 15}}")
        print(f"\tГод издания:{year_prefix(data['year']):>{self.MAX_LEN - 21}}\n")
        ans = input("Добавить? (Введите нет для отмены)")
        if ans.lower() != "нет":
            return
        #TODO Доделать

    def clear(self):
        os.system("cls")



