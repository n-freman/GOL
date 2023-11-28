import typer

from gol.entrypoints.cli.utils import (
    logo,
    get_table,
)
from gol.service_layer import services
from gol.service_layer.uow import SQLModelUnitOfWork

app = typer.Typer()


@app.command()
def add_action():
    print(logo, '\n')
    title = input('Title: ')
    score = float(input('Score: '))
    uow = SQLModelUnitOfWork()
    try:
        services.add_action(title, score, uow)
    except Exception as e:
        print(e)
        print('Error ocurred')


@app.command()
def weekly_actions():
    print(logo, '\n')
    uow = SQLModelUnitOfWork()
    try:
        actions = services.weekly_actions(uow)
        print(get_table(actions))
    except Exception as e:
        print(e)

