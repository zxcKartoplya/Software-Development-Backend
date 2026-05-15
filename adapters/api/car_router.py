from fastapi import APIRouter, Depends, HTTPException

from adapters.api.dependencies import get_car_repository
from adapters.api.schemas import CarRequest, CarResponse
from domain.entities.car import Car
from domain.exceptions import CarNotFoundError
from domain.repositories.car_repository import CarRepository
from use_cases.create_car import CreateCarUseCase
from use_cases.delete_car import DeleteCarUseCase
from use_cases.get_car import GetCarUseCase
from use_cases.get_cars import GetCarsUseCase
from use_cases.update_car import UpdateCarUseCase

router = APIRouter(prefix="/cars", tags=["cars"])


@router.get("", response_model=list[CarResponse])
def get_cars(repo: CarRepository = Depends(get_car_repository)):
    cars = GetCarsUseCase(repo).execute()
    return [CarResponse.model_validate(car, from_attributes=True) for car in cars]


@router.get("/{car_id}", response_model=CarResponse)
def get_car(car_id: int, repo: CarRepository = Depends(get_car_repository)):
    try:
        car = GetCarUseCase(repo).execute(car_id)
        return CarResponse.model_validate(car, from_attributes=True)
    except CarNotFoundError:
        raise HTTPException(status_code=404, detail="Car not found")


@router.post("", response_model=CarResponse, status_code=201)
def create_car(data: CarRequest, repo: CarRepository = Depends(get_car_repository)):
    car = Car(**data.model_dump())
    created = CreateCarUseCase(repo).execute(car)
    return CarResponse.model_validate(created, from_attributes=True)


@router.put("/{car_id}", response_model=CarResponse)
def update_car(car_id: int, data: CarRequest, repo: CarRepository = Depends(get_car_repository)):
    try:
        car = Car(id=car_id, **data.model_dump())
        updated = UpdateCarUseCase(repo).execute(car)
        return CarResponse.model_validate(updated, from_attributes=True)
    except CarNotFoundError:
        raise HTTPException(status_code=404, detail="Car not found")


@router.delete("/{car_id}")
def delete_car(car_id: int, repo: CarRepository = Depends(get_car_repository)):
    try:
        DeleteCarUseCase(repo).execute(car_id)
        return {"message": "Car deleted"}
    except CarNotFoundError:
        raise HTTPException(status_code=404, detail="Car not found")
