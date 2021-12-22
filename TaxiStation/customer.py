from dataclasses import dataclass
from TaxiStation.recipts_factory import ReciptType


@dataclass
class CustomerType:
    buisness = "b"
    private = "p"


@dataclass
class Customer:
    type: CustomerType
    num_of_passengers: int
    distance: int
    recipt_type: ReciptType = ReciptType.TEXT
