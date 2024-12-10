import datetime

from pydantic import BaseModel, Field, ConfigDict

class RouteSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number_of_route: int
    number_of_starting_port: int
    number_of_ending_Port: int
    route_length: int