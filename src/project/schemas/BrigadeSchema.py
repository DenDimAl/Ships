import datetime

from pydantic import BaseModel, Field, ConfigDict

class BrigadeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number_of_brigade: int
    signed_employee: str