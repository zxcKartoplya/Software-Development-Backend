from __future__ import annotations

from domain.entities.car import Car
from domain.repositories.car_repository import CarRepository


class GetCarsUseCase:
    def __init__(self, repo: CarRepository):
        self.repo = repo

    def execute(self) -> list[Car]:
        return self.repo.get_all()
