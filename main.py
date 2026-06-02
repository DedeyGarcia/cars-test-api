from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from decimal import Decimal
from enum import Enum

app = FastAPI(title="Cars API", description="API de carros para testes de frontend")

# ── Enums ──────────────────────────────────────────────────────────────────────

class CarState(str, Enum):
    novo = "Novo"
    seminovo = "Seminovo"

class FuelType(str, Enum):
    gasolina = "Gasolina"
    etanol = "Etanol"
    flex = "Flex"
    diesel = "Diesel"
    eletrico = "Elétrico"
    hibrido = "Híbrido"

class TransmissionType(str, Enum):
    manual = "Manual"
    automatico = "Automático"
    cvt = "CVT"

# ── Models ─────────────────────────────────────────────────────────────────────

class CarBase(BaseModel):
    marca: str = Field(..., examples=["Toyota"])
    modelo: str = Field(..., examples=["Corolla"])
    ano: int = Field(..., ge=1886, le=2100, examples=[2023])
    estado: CarState = Field(..., examples=[CarState.novo])
    motor: str = Field(..., examples=["2.0 16V"])
    combustivel: FuelType = Field(..., examples=[FuelType.flex])
    transmissao: TransmissionType = Field(..., examples=[TransmissionType.automatico])
    cor: str = Field(..., examples=["Prata"])
    quilometragem: int = Field(default=0, ge=0, examples=[15000])
    preco: Decimal = Field(..., gt=0, decimal_places=2, examples=[120000.00])
    image_url: Optional[str] = Field(default=None, examples=["https://example.com/carro.jpg"])

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    pass

class CarPatch(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = Field(default=None, ge=1886, le=2100)
    estado: Optional[CarState] = None
    motor: Optional[str] = None
    combustivel: Optional[FuelType] = None
    transmissao: Optional[TransmissionType] = None
    cor: Optional[str] = None
    quilometragem: Optional[int] = Field(default=None, ge=0)
    preco: Optional[Decimal] = Field(default=None, gt=0, decimal_places=2)
    image_url: Optional[str] = None

class Car(CarBase):
    id: UUID

    model_config = {"from_attributes": True}

# ── In-memory store ────────────────────────────────────────────────────────────

db: dict[UUID, Car] = {}

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/cars", response_model=list[Car], tags=["cars"])
def list_cars():
    return list(db.values())


@app.get("/cars/{car_id}", response_model=Car, tags=["cars"])
def get_car(car_id: UUID):
    car = db.get(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return car


@app.post("/cars", response_model=Car, status_code=201, tags=["cars"])
def create_car(data: CarCreate):
    car = Car(id=uuid4(), **data.model_dump())
    db[car.id] = car
    return car


@app.put("/cars/{car_id}", response_model=Car, tags=["cars"])
def replace_car(car_id: UUID, data: CarUpdate):
    if car_id not in db:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    car = Car(id=car_id, **data.model_dump())
    db[car_id] = car
    return car


@app.patch("/cars/{car_id}", response_model=Car, tags=["cars"])
def update_car(car_id: UUID, data: CarPatch):
    car = db.get(car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    updated = car.model_dump()
    updated.update({k: v for k, v in data.model_dump().items() if v is not None})
    db[car_id] = Car(**updated)
    return db[car_id]


@app.delete("/cars/{car_id}", status_code=204, tags=["cars"])
def delete_car(car_id: UUID):
    if car_id not in db:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    del db[car_id]
