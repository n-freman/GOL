from art import text2art
from tabulate import tabulate

logo = text2art('G-O-L', font='tarty1')


def get_table(data):
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
