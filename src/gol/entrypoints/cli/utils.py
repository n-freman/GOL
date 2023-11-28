import os

from art import text2art
from tabulate import tabulate


def get_centered_table(data) -> str:
    return center(get_table(data))


def get_table(data) -> str:
    rows = []
    for record in data:
        rows.append([
            record.title,
            record.score,
            record.date_added.strftime('%Y-%m-%d')
        ])
    return tabulate(
        rows,
        ['title', 'score', 'date'],
        'heavy_outline'
    )


def center(text: str) -> str:
    width = os.get_terminal_size()[0]
    lines = text.split('\n')
    return "\n".join(line.center(width) for line in lines)


logo = center(text2art('G-O-L', font='tarty1'))

