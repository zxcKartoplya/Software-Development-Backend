from __future__ import annotations

import pytest

from domain.exceptions import CarNotFoundError
from use_cases.get_car import GetCarUseCase


def test_get_car_returns_car_when_exists(repo, sample_car):
    result = GetCarUseCase(repo).execute(car_id=1)
    assert result == sample_car


def test_get_car_raises_when_not_found(empty_repo):
    with pytest.raises(CarNotFoundError):
        GetCarUseCase(empty_repo).execute(car_id=99)
