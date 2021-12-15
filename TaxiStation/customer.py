from dataclasses import dataclass


@dataclass
class CustomerType:
    buisness = "b"
    private = "p"


@dataclass
class Customer:
    type: CustomerType
    num_of_passengers: int
    distance: int
