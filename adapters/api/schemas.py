from pydantic import BaseModel

from domain.entities.car import AssemblyType, BodyType


class CarRequest(BaseModel):
    body_type: BodyType
    seats_count: int
    engine_type: str
    engine_power: int
    transmission_type: str
    assembly_type: AssemblyType


class CarResponse(BaseModel):
    id: int
    body_type: BodyType
    seats_count: int
    engine_type: str
    engine_power: int
    transmission_type: str
    assembly_type: AssemblyType

    model_config = {"from_attributes": True}
