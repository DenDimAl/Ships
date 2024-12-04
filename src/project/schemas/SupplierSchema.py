import datetime

from pydantic import BaseModel, Field, ConfigDict

class SupplierSchema(BaseModel):
    face_number: int
    name_of_the_firm: str
    accompalience_date: datetime
    state_or_private: bool