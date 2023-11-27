import typer

from gol.entrypoints.cli.utils import logo
from gol.service_layer import services
from gol.service_layer.uow import SQLModelUnitOfWork

app = typer.Typer()


@app.command()
def add_action():
    print(logo)
    title = input('Title: ')
    score = float(input('Score: '))
    uow = SQLModelUnitOfWork()
    try:
        services.add_action(title, score, uow)
    except Exception as e:
        print(e)
        print('Error ocurred')

