from TaxiStation.cars import Car, Taxi, Lemo, Van, Minibus
from copy import deepcopy
from logging import warning
from TaxiStation.customer import Customer, CustomerType

from TaxiStation.utils import get_type_name


car_types_by_name = {
    car_type.__name__: car_type for car_type in (Taxi, Lemo, Van, Minibus)
}


class CarFleet:
    def __init__(self, cars: list = None) -> None:
        self._data = {}
        if cars:
            self._load_from_list(self._data, cars)

    def __setitem__(self, key, value) -> None:
        if not isinstance(value, Car):
            self._load_from_list(self._data, value)
        else:
            type_name = get_type_name(value)
            if type_name != key or key not in car_types_by_name.keys():
                raise TypeError(
                    f"{CarFleet.__name__} accepts only supported keys and values. got '{key}:{type_name}'"
                )
            else:
                self._data[type_name] = self._data.get(type_name, []) + [value]

    def __getitem__(self, key):
        try:
            return next(
                (
                    car
                    for car in self._data.get(key, [])
                    if car.available and self._data.get(key)
                )
            )
        except StopIteration:
            return None

    @staticmethod
    def _load_from_list(data, cars):
        for car in cars:
            type_name = get_type_name(car)
            if type_name not in car_types_by_name.keys():
                raise TypeError(
                    f"{CarFleet.__name__} accepts only supported cars: {tuple(car_types_by_name.keys())}. but got '{type_name}'"
                )
            data[type_name] = data.get(type_name, []) + [car]

    def to_dict(self):
        return deepcopy(self._data)

    def car_types(self):
        return tuple(self._data.keys)

    def from_dict(self, cars_dict):
        for lst in cars_dict:
            self[""] = lst

    def __repr__(self) -> str:

        return (
            "CarFleet:\n"
            + ", ".join(
                (f"total {kind}: {len(lst)}" for kind, lst in self._data.items())
            )
            + "\n"
            + ", ".join(
                (
                    f"available {kind}: {len([car for car in self._data[kind] if car.available])}"
                    for kind in self._data
                )
            )
        )


class TaxiStation:
    MAX_CARS_NUMBER = 30

    def __init__(self, cars_dict: dict = None) -> None:
        if not cars_dict:
            cars_dict = {name: [] for name in car_types_by_name.keys()}
        self._cars = CarFleet.validate_cars_dict(cars_dict, False)

    def work(self, clients: list[Customer]):

        customers = clients.copy()
        waiting_customers = []
        while customers:
            # get first
            cust = customers.pop(0)

            # decide what is the right type
            if cust.type == CustomerType.buisness:
                wanted_type = Lemo
            else:
                if cust.num_of_passengers <= Taxi.SEATS:
                    wanted_type = Taxi
                elif cust.num_of_passengers <= Van.SEATS:
                    wanted_type = Van
                elif cust.num_of_passengers <= Minibus.SEATS:
                    wanted_type = Minibus
                else:
                    raise NotImplementedError("handle this")
                wanted_type = get_type_name(wanted_type)

        # find a taxi
        avl_car = self.cars[wanted_type]
        if avl_car:
            avl_car.drive()
        else:
            if wanted_type in self.cars.car_types():
                # he will wait for the right taxi to return
                waiting_customers.append(cust)
            else:
                raise NotImplementedError("handle this")

    @property
    def cars(self):
        return self._cars.to_dict()

    @cars.setter
    def cars(self, v: dict):
        self._cars.from_dict(v)
