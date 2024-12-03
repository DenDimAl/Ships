import datetime

from pydantic import BaseModel, Field, ConfigDict

class GateSchema(BaseModel):
    NumberOfGate: int
    NumberInPort: int
    NumberOfPort: int
    NumberOfCrane: int