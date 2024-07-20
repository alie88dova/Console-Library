# -*- coding: utf-8 -*-
from enum import Enum
from datetime import datetime
from hashlib import sha256


class Status(Enum):
    given = "Выдана"
    available = "В наличии"


class Book:
    """
    Хранит информацию об отдельном экзэмпляре книги из библиотеки
    id - str уникальный идентификатор книги
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
        self.year = year
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
