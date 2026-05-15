from sqlalchemy import Column, Integer, String

from infrastructure.database import Base


class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    body_type = Column(String, nullable=False)
    seats_count = Column(Integer, nullable=False)
    engine_type = Column(String, nullable=False)
    engine_power = Column(Integer, nullable=False)
    transmission_type = Column(String, nullable=False)
    assembly_type = Column(String, nullable=False)
