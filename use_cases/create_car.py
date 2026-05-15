from domain.repositories.car_repository import CarRepository
from domain.entities.car import Car


class CreateCarUseCase:
    def __init__(self, repo: CarRepository):
        self.repo = repo

    def execute(self, car: Car) -> Car:
        return self.repo.save(car)
