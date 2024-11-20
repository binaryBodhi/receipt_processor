from pydantic import BaseModel
from typing import List

# ITEM SCHEMA
class ItemSchema(BaseModel):
    shortDescription: str
    price: str

# RECEIPT SCHEMA
class ReceiptSchema(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[ItemSchema]
    total: str
