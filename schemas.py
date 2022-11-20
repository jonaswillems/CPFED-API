#Created by Jonas Willems.
#!/usr/bin/env python3


from pydantic import BaseModel


class APIBase(BaseModel):
    Id: int
    storeName: str
    drinkName: str
    drinkPrice: float

    class Config:
        orm_mode = True

class APICreate(BaseModel):
    pass

    class Config:
        orm_mode = True

