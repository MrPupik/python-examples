from TaxiStation import cars
from . import UnsuportedOperationException
from TaxiStation.cars import Taxi, Lemo, Van, Minibus
from copy import deepcopy


def a(b: int = 5):
    pass


class TaxiStation:
    MAX_CARS_NUMBER = 30

    def __init__(self, cars_dict: dict = None) -> None:
        self._cars = cars_dict
        TaxiStation.validate_cars_dict(self.cars, False)

    @property
    def cars(self):
        return deepcopy(self._cars)

    @property.setter
    def cars(self, new_dict):
        self._cars = TaxiStation.validate_cars_dict(new_dict)

    @staticmethod
    def validate_cars_dict(cars_dict, silent_mode=True):
        """validating cars dict and returns it.

        `cars_dict`: the dict
        `silent_mode`: when False, throws exception if dict is not valid. else returns None"""
