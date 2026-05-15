from domain.exceptions import CarNotFoundError
from domain.repositories.car_repository import CarRepository


class DeleteCarUseCase:
    def __init__(self, repo: CarRepository):
        self.repo = repo

    def execute(self, car_id: int) -> None:
        if self.repo.get_by_id(car_id) is None:
            raise CarNotFoundError(car_id)
        self.repo.delete(car_id)
