# -*- coding: utf-8 -*-
from json import dump, load
from os import curdir


def save(data: dict) -> bool:
    """
    Сохраняет данные в нашу библ1
    :param data:
    :return bool:
    """
    with open(f"{curdir}/books.json", "w") as f:
        dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )
    return True


def upload():
    """"""
    with open(f"{curdir}/books.json", 'r', encoding='utf-8') as f:
        return load(f)