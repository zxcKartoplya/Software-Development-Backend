from __future__ import annotations

from sqlalchemy.orm import Session

from domain.entities.car import AssemblyType, BodyType, Car
from domain.repositories.car_repository import CarRepository
from infrastructure.models import CarModel


class SQLiteCarRepository(CarRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Car]:
        return [self._to_entity(m) for m in self.db.query(CarModel).all()]

    def get_by_id(self, car_id: int) -> Car | None:
        model = self.db.query(CarModel).filter(CarModel.id == car_id).first()
        return self._to_entity(model) if model else None

    def save(self, car: Car) -> Car:
        model = CarModel(
            body_type=car.body_type,
            seats_count=car.seats_count,
            engine_type=car.engine_type,
            engine_power=car.engine_power,
            transmission_type=car.transmission_type,
            assembly_type=car.assembly_type,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return self._to_entity(model)

    def update(self, car: Car) -> Car:
        model = self.db.query(CarModel).filter(CarModel.id == car.id).first()
        model.body_type = car.body_type
        model.seats_count = car.seats_count
        model.engine_type = car.engine_type
        model.engine_power = car.engine_power
        model.transmission_type = car.transmission_type
        model.assembly_type = car.assembly_type
        self.db.commit()
        self.db.refresh(model)
        return self._to_entity(model)

    def delete(self, car_id: int) -> None:
        model = self.db.query(CarModel).filter(CarModel.id == car_id).first()
        self.db.delete(model)
        self.db.commit()

    def _to_entity(self, model: CarModel) -> Car:
        return Car(
            id=model.id,
            body_type=BodyType(model.body_type),
            seats_count=model.seats_count,
            engine_type=model.engine_type,
            engine_power=model.engine_power,
            transmission_type=model.transmission_type,
            assembly_type=AssemblyType(model.assembly_type),
        )
