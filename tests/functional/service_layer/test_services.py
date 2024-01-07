from datetime import date

import pytest
from unittest import mock

from gol.service_layer import services


@pytest.fixture
def current_week_actions():
    pass


@pytest.fixture
def another_week_actions():
    pass


@pytest.fixture
def uow():
    uow_ = mock.MagicMock()
    return uow_


def test_add_action_success(uow):
    action_title = 'generic action'
    action_score = 4.20

    uow.actions.add.return_value = services.Action(
        title=action_title,
        score=action_score
    )

    result = services.add_action(
        action_title,
        action_score,
        uow
    )

    uow.actions.add.assert_called_once_with(
        title=action_title,
        score=action_score
    )
    uow.commit.assert_called_once_with()

    assert result is uow.actions.add.return_value
    


def test_weekly_actions(uow):
    actions = [
        services.Action(
            title=f'action #{i}',
            score=7.40*(-1)**i,
            date_added=date.today()
        )
        for i in range(10)
    ]
    uow.actions.list.return_value = actions

    result = services.weekly_actions(uow)

    assert result is actions


def test_calc_last_week_total_score_counts_all_last_week_acitons(
    uow,
    current_week_actions
):
    pytest.fail()


def test_calc_last_week_total_score_not_count_other_week_actions(
    uow,
    current_week_actions,
    other_week_actions,
):
    pytest.fail()

