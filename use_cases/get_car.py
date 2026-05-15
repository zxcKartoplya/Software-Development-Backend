from domain.entities.car import Car
from domain.exceptions import CarNotFoundError
from domain.repositories.car_repository import CarRepository


class GetCarUseCase:
    def __init__(self, repo: CarRepository):
        self.repo = repo

    def execute(self, car_id: int) -> Car:
        car = self.repo.get_by_id(car_id)
        if car is None:
            raise CarNotFoundError(car_id)
        return car
