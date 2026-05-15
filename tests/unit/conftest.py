from __future__ import annotations

import pytest

from domain.entities.car import AssemblyType, BodyType, Car
from domain.repositories.car_repository import CarRepository


class FakeCarRepository(CarRepository):
    def __init__(self, cars: list[Car]):
        self._store: dict[int, Car] = {car.id: car for car in cars}

    def get_all(self) -> list[Car]:
        return list(self._store.values())

    def get_by_id(self, car_id: int) -> Car | None:
        return self._store.get(car_id)

    def save(self, car: Car) -> Car:
        car.id = max(self._store.keys(), default=0) + 1
        self._store[car.id] = car
        return car

    def update(self, car: Car) -> Car:
        self._store[car.id] = car
        return car

    def delete(self, car_id: int) -> None:
        self._store.pop(car_id, None)


@pytest.fixture
def sample_car() -> Car:
    return Car(
        id=1,
        body_type=BodyType.sedan,
        seats_count=5,
        engine_type="Petrol",
        engine_power=150,
        transmission_type="Automatic",
        assembly_type=AssemblyType.auto,
    )


@pytest.fixture
def repo(sample_car) -> FakeCarRepository:
    return FakeCarRepository([sample_car])


@pytest.fixture
def empty_repo() -> FakeCarRepository:
    return FakeCarRepository([])
