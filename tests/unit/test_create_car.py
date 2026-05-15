from __future__ import annotations

from domain.entities.car import AssemblyType, BodyType, Car
from use_cases.create_car import CreateCarUseCase


def test_create_car_saves_and_returns_car(empty_repo):
    car = Car(
        body_type=BodyType.hatchback,
        seats_count=4,
        engine_type="Diesel",
        engine_power=120,
        transmission_type="Manual",
        assembly_type=AssemblyType.manual,
    )

    result = CreateCarUseCase(empty_repo).execute(car)

    assert result.id is not None
    assert result.body_type == BodyType.hatchback
