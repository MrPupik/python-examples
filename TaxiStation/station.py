from sys import stdout
from TaxiStation.cars import Car, Taxi, Lemo, Van, Minibus
from copy import deepcopy

import logging
from TaxiStation.customer import Customer, CustomerType

from TaxiStation.utils import get_type_name

logging.basicConfig(filename='taxi_station.log',
                    encoding='utf-8', level=logging.DEBUG)
info = logging.info

logging.getLogger().addHandler(logging.StreamHandler())


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
        for car in self._data.get(key, []):
            if car.available and self._data.get(key):
                return car

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
        return tuple(self._data.keys())

    def from_dict(self, cars_dict):
        for lst in cars_dict:
            self[""] = lst

    def __repr__(self) -> str:

        return (
            "CarFleet:\n"
            + ", ".join(
                (f"total {kind}: {len(lst)}" for kind,
                 lst in self._data.items())
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
    HELP_WAITING = True

    def __init__(self, cars: CarFleet) -> None:
        self.cars = cars
        self.money = 0
        self.owed_money = 0

    def work(self, clients: list[Customer], trip_number=0):

        customers = clients.copy()
        self.waiting_customers = []
        self.disappointed = []
        self.trip_number = trip_number

        while customers or self.waiting_customers:
            # get first
            self.trip_number += 1

            if customers:
                cust = customers.pop(0)

            # initail help vars
            cust.trip_number = self.trip_number
            cust.bill = 0

            info(
                f"new customer {cust.trip_number}, type:{cust.type} quantity:{cust.num_of_passengers}")
            wanted_type = self._classifiy(cust)

            if not wanted_type:
                continue
            else:
                cust.wanted_type = wanted_type

            # try find for waiting_cust
            if self.waiting_customers and self.HELP_WAITING:
                waiting_cust = self.waiting_customers.pop(0)
                car = self._find_car(waiting_cust)
                if car:
                    car.drive(waiting_cust.distance)
            car = self._find_car(cust)
            if car:
                car.drive(cust.distance)

    def _find_car(self, cust) -> Car | None:
        avl_car = self.cars[cust.wanted_type]
        if avl_car:
            info(f"found available {cust.wanted_type}, driving...")
            return avl_car

        if cust.wanted_type in self.cars.car_types():
            info(
                f"did not find available {cust.wanted_type}. adding to line")
            # he will wait for the right taxi to return
            self.waiting_customers.append(cust)
        else:
            self.disappointed.append(cust)
            info(
                f"no {cust.wanted_type} in station, customer added to disappointed")

    def _classifiy(self, cust: Customer) -> str | None:
        """determine what car is good for this customer"""

        # decide what is the right type
        if cust.type == CustomerType.buisness:
            if cust.num_of_passengers > 100:
                self.disappointed.append(cust)
                info(f"customer {cust.trip_number} added to disappointed")
            else:
                return Lemo.__name__
        else:
            if cust.num_of_passengers <= Taxi.SEATS:
                return Taxi.__name__
            elif cust.num_of_passengers <= Van.SEATS:
                return Van.__name__
            elif cust.num_of_passengers <= Minibus.SEATS:
                return Minibus.__name__
            else:
                self.disappointed.append(cust)
                info(f"customer {cust.trip_number} added to disappointed")

    def _drive_customer(self, car: Car, cust: Customer):
        price, dist_travelled = car.drive(cust.distance)
        if dist_travelled < cust.distance:
            info(
                f"cust {cust.trip_number} drove {dist_travelled} out of {cust.distance}")
            self.waiting_customers.append(cust)
            # discount for partial trip
            price = 0.85 * price
            cust.bill += price  # maybe discount entire bill ?
            info(
                f"cust {cust.trip_number} drove {dist_travelled} out of {cust.distance}. it costs {price} and it's current bill is {cust.bill}")
        else:
            info(
                f"cust {cust.trip_number} reached destination (after {dist_travelled}).")

            self._charge(cust)

    def _charge(self, cust: Customer):
        self.money += cust.bill
        info(
            f"charged {cust.bill} from {cust.trip_number}. balance: {self.money}")
