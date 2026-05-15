from __future__ import annotations

from use_cases.get_cars import GetCarsUseCase


def test_get_cars_returns_all(repo, sample_car):
    result = GetCarsUseCase(repo).execute()
    assert result == [sample_car]


def test_get_cars_returns_empty_list(empty_repo):
    result = GetCarsUseCase(empty_repo).execute()
    assert result == []
