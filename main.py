from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import infrastructure.models  # noqa: F401 — registers ORM models with Base
from adapters.api.car_router import router
from infrastructure.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Factory API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
