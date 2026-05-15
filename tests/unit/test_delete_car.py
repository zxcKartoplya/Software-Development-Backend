from __future__ import annotations

import pytest

from domain.exceptions import CarNotFoundError
from use_cases.delete_car import DeleteCarUseCase
from use_cases.get_cars import GetCarsUseCase


def test_delete_car_removes_car(repo):
    DeleteCarUseCase(repo).execute(car_id=1)
    assert GetCarsUseCase(repo).execute() == []


def test_delete_car_raises_when_not_found(empty_repo):
    with pytest.raises(CarNotFoundError):
        DeleteCarUseCase(empty_repo).execute(car_id=99)
