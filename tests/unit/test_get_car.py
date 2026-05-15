from __future__ import annotations

from domain.entities.car import AssemblyType, BodyType, Car
from domain.exceptions import CarNotFoundError
from domain.repositories.car_repository import CarRepository
from use_cases.get_car import GetCarUseCase


class FakeCarRepository(CarRepository):
    """In-memory реализация CarRepository для тестов. Не трогает БД."""

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


def _sample_car(id: int = 1) -> Car:
    return Car(
        id=id,
        body_type=BodyType.sedan,
        seats_count=5,
        engine_type="Petrol",
        engine_power=150,
        transmission_type="Automatic",
        assembly_type=AssemblyType.auto,
    )


# --- тесты ---

def test_get_car_returns_car_when_exists():
    car = _sample_car(id=1)
    repo = FakeCarRepository([car])

    result = GetCarUseCase(repo).execute(car_id=1)

    assert result == car
