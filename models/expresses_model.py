from pydantic import BaseModel

class Express(BaseModel):
    weight: str
    price: str
    region: str