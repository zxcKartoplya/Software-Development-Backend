from __future__ import annotations

import pytest

from domain.entities.car import AssemblyType, BodyType, Car
from domain.exceptions import CarNotFoundError
from use_cases.update_car import UpdateCarUseCase


def test_update_car_changes_fields(repo, sample_car):
    updated = Car(
        id=sample_car.id,
        body_type=BodyType.wagon,
        seats_count=7,
        engine_type="Diesel",
        engine_power=200,
        transmission_type="Manual",
        assembly_type=AssemblyType.manual,
    )

    result = UpdateCarUseCase(repo).execute(updated)

    assert result.body_type == BodyType.wagon
    assert result.seats_count == 7


def test_update_car_raises_when_not_found(empty_repo, sample_car):
    with pytest.raises(CarNotFoundError):
        UpdateCarUseCase(empty_repo).execute(sample_car)
