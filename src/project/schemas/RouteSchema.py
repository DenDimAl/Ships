import datetime

from pydantic import BaseModel, Field, ConfigDict

class RouteSchema(BaseModel):
    NumberOfRoute: int
    NumberOfStartingPoint: int
    NumberOfEndingPoint: int
    RouteLengrh: int