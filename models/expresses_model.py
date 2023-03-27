from pydantic import BaseModel

class Express(BaseModel):
    weight: str
    price1: str
    region1: str
    price2: str
    region2: str
