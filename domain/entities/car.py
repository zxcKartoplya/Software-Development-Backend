from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BodyType(str, Enum):
    sedan = "Sedan"
    hatchback = "Hatchback"
    wagon = "Wagon"


class AssemblyType(str, Enum):
    auto = "AUTO"
    manual = "MANUAL"


@dataclass
class Car:
    body_type: BodyType
    seats_count: int
    engine_type: str
    engine_power: int
    transmission_type: str
    assembly_type: AssemblyType
    id: Optional[int] = None
