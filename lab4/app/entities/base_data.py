from pydantic import BaseModel


class AccelerometerData(BaseModel):
    x: float
    y: float
    z: float


class GpsData(BaseModel):
    latitude: float
    longitude: float

class ParkingData(BaseModel):
    empty_count: float
    gps: GpsData
