from __future__ import annotations

from abc import ABC, abstractmethod

from domain.entities.car import Car


class CarRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Car]: ...

    @abstractmethod
    def get_by_id(self, car_id: int) -> Car | None: ...

    @abstractmethod
    def save(self, car: Car) -> Car: ...

    @abstractmethod
    def update(self, car: Car) -> Car: ...

    @abstractmethod
    def delete(self, car_id: int) -> None: ...
