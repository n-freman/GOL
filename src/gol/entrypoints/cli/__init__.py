import typer

from gol.entrypoints.cli.utils import center, get_centered_table, logo
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
    else:
        print(center('Successfully added action!'))


@app.command()
def weekly_actions():
    print(logo, '\n')
    uow = SQLModelUnitOfWork()
    try:
        actions = services.weekly_actions(uow)
        print(get_centered_table(actions))
        print(center(
            f'\nTotal: {services.calc_last_week_total_score(uow)}'
        ))
    except Exception as e:
        print(e)

