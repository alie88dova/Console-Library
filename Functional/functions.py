# -*- coding: utf-8 -*-
from Models.Book import Book
from DataBaseTools.tools import upload

def year_prefix(year: str) -> str:

    if year == "None":
        return f"None"
    elif int(year) > 0:
        return f"{year} год"
    else:
        return f"{year} году до Н.Э"


def load_list_books() -> list[Book]:
    """Выгружает из словаря выгруженного из нашего json файла """
    data = upload()
    lib = []
    for b in data:
        book = Book(
            title=b['title'],
            year=b['year'],
            status=b['status'],
            author=b['author'],
            date_add=b['date_add'],
            date_last_given=b['date_last_login']
        )
        book.id = b['id']
        lib.append(book)

    return lib






if __name__ == '__main__':
    pass
