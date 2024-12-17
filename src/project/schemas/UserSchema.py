from pydantic import BaseModel, Field, ConfigDict

class UserCreateUpdateSchema(BaseModel):
    first_name: str
    second_name: str
    email: str = Field(pattern=r"^\S+@\S+\.\S+$", examples=["email@mail.ru"])
    password: str
    is_admin: bool = False


class UserSchema(UserCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int