from domain.entities.car import Car
from domain.exceptions import CarNotFoundError
from domain.repositories.car_repository import CarRepository


class UpdateCarUseCase:
    def __init__(self, repo: CarRepository):
        self.repo = repo

    def execute(self, car: Car) -> Car:
        if self.repo.get_by_id(car.id) is None:
            raise CarNotFoundError(car.id)
        return self.repo.update(car)
