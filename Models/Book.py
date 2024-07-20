# -*- coding: utf-8 -*-
from enum import Enum
from datetime import datetime
from hashlib import sha256


class Status(Enum):
    given = "Выдана"
    available = "В наличии"


class Book:
    """
    Хранит информацию об отдельном экземпляре книги из библиотеки
    id - str уникальный идентификатор книги
    author - str автор книги, если автора нет хранит 'Автора нет'
    title - str хранит название книги
    year - int хранит год издания книги
    status - str хранит информацию о статусе книги (Может принимать значения только из Status)
    date_add - datetime время добавления книги в библиотеку, если значение при создании не указано, то равняется
                текущему
    date_last_given - datetime время последней выдачи книги
    """
    def __init__(
            self,
            title: str,
            year: int,
            status: str,
            date_add: datetime = datetime.now(),
            date_last_given: datetime = None,
            author: str = "Автора нет",
                 ):
        self.id = self.generate_id()
        self.title = title
        self.year = self.check_year(year)
        self.status = status
        self.date_add = date_add
        self.date_last_given = date_last_given
        self.author = author

    @staticmethod
    def generate_id() -> str:
        """
        Генерирует Уникальный идентификатор с помощью sha256
        :return str Уник. идентификатор:
        """
        salt = "1234abcdABCD5678"
        string = salt + str(datetime.now())

        return sha256(string.encode()).hexdigest()

    @staticmethod
    def check_year(year) -> int:
        if year <= -2000 or year >= datetime.year: # Отрицательные значения до нашей эры
            raise Exception("Невозможный год издания")
        return year

    def update_title(self, title: str):
        """
        Изменяет значение title на переданное
        :param title:
        """
        self.title = title

    def update_year(self, year: int):
        """
        Изменяет значение year на переданное
        :param year:
        """
        self.year = self.check_year(year)

    def update_author(self, author="Автора нет"):
        """
        Изменяет значение author на переданное
        :param author:
        """
        self.author = author

    def book_return(self):
        """
        Изменяет статус книги на 'В наличии'
        """
        self.status = Status.available

    def book_give(self):
        """
        Изменяет статус книги на 'Выдана'
        """
        self.status = Status.given
        self.date_last_given = datetime.now()

    def get_json_file(self) -> dict:
        """Возвращает словарь готовый к упаковке в json"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
            "date_add": self.date_add,
            "date_last_given": self.date_last_given,
        }
    